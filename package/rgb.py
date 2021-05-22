def to_hex(r, g, b):
    hex = "#"

    for x in [r, g, b]:
        hex += format(x, "x").rjust(2, "0")

    return hex


def to_ints(hex):
    r = hex[1:3]
    g = hex[3:5]
    b = hex[5:7]
    return list(map(lambda x: int(x, base=16), [r, g, b]))
