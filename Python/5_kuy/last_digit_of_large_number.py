def last_digit(n1: int, n2: int) -> int:
    return pow(n1, n2, 10)


if __name__ == "__main__":
    print(last_digit(2 ** 200, 2 ** 300))

"""
rules = {
    0: [0,0,0,0],
    1: [1,1,1,1],
    2: [2,4,8,6],
    3: [3,9,7,1],
    4: [4,6,4,6],
    5: [5,5,5,5],
    6: [6,6,6,6],
    7: [7,9,3,1],
    8: [8,4,2,6],
    9: [9,1,9,1],
}
def last_digit(n1, n2):
    ruler = rules[int(str(n1)[-1])]
    return 1 if n2 == 0 else ruler[(n2 % 4) - 1]


def last_digit(n1, n2):
    return (n1 % 10) ** (n2 % 4 + 4 * bool(n2)) % 10
"""
