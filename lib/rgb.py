def to_hex(r, g, b):
    return (
        "#"
        + format(r, "x").rjust(2, "0")
        + format(g, "x").rjust(2, "0")
        + format(b, "x").rjust(2, "0")
    )
