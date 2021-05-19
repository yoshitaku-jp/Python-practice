def to_hex(r, g, b):
    hex = "#"

    for x in [r, g, b]:
        hex += format(x, "x").rjust(2, "0")

    return hex
