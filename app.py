from flask import Flask, jsonify, render_template, request

from converter import SUPPORTED_UNITS, convert

app = Flask(__name__)

APP_VERSION = "1.0.0"


@app.route("/")
def index():
    result = None
    error = None
    value = request.args.get("value")
    src = request.args.get("src", "c")
    dst = request.args.get("dst", "f")

    if value:
        try:
            result = convert(float(value), src, dst)
        except ValueError as exc:
            error = str(exc)

    return render_template(
        "index.html",
        units=SUPPORTED_UNITS,
        value=value or "",
        src=src,
        dst=dst,
        result=result,
        error=error,
    )


@app.route("/api/convert")
def api_convert():
    try:
        value = float(request.args["value"])
        src = request.args["src"]
        dst = request.args["dst"]
        result = convert(value, src, dst)
    except KeyError as exc:
        return jsonify(error=f"Не передан параметр {exc.args[0]}"), 400
    except ValueError as exc:
        return jsonify(error=str(exc)), 400
    return jsonify(value=value, src=src, dst=dst, result=result)


@app.route("/version")
def version():
    return jsonify(version=APP_VERSION)


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
