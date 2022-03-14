from math import factorial


def pascals_triangle(n: int) -> list:
    triangle = []
    for i in range(n):
        triangle.extend(
            factorial(i) // (factorial(j) * factorial(i - j))
            for j in range(i + 1)
        )

    return triangle


if __name__ == "__main__":
    pass
