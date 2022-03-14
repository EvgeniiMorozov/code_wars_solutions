from math import pi, acos, sqrt


def tankvol(h, d, vt):
    r = d / 2
    w = vt / (r**2 * pi)
    a = r**2 * acos(1 - h / r) - (r - h) * sqrt(2 * r * h - h**2)
    return int(w * a)


if __name__ == "__main__":
    pass
