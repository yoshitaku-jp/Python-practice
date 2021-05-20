def to_hex(r, g, b):
    hex = "#"

    for x in [r, g, b]:
        hex += format(x, "x").rjust(2, "0")

    return hex


def to_ints(hex):
    r = hex[1:3]
    g = hex[3:5]
    b = hex[5:7]
    ints = []
    for i in [r, g, b]:
        ints.append(int(i, base=16))
    return ints
