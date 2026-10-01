"""Логика конвертации температур (отделена от веб-слоя, чтобы её было удобно тестировать)."""

SUPPORTED_UNITS = ("c", "f", "k")
ABSOLUTE_ZERO_C = -273.15


def to_celsius(value, unit):
    if unit == "c":
        return value
    if unit == "f":
        return (value - 32) * 5 / 9
    if unit == "k":
        return value - 273.15
    raise ValueError(f"Неизвестная единица измерения: {unit}")


def from_celsius(value, unit):
    if unit == "c":
        return value
    if unit == "f":
        return value * 9 / 5 + 32
    if unit == "k":
        return value + 273.15
    raise ValueError(f"Неизвестная единица измерения: {unit}")


def convert(value, src, dst):
    src = src.lower()
    dst = dst.lower()
    celsius = to_celsius(value, src)
    if celsius < ABSOLUTE_ZERO_C:
        raise ValueError("Температура ниже абсолютного нуля")
    return round(from_celsius(celsius, dst), 2)
