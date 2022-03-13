from collections import deque


def shifted_diff(first: str, second: str) -> int:
    if first == second:
        return 0
    if len(first) != len(second):
        return -1
    if not all([el[0] == el[1] for el in zip(sorted(first), sorted(second))]):
        return -1

    first_deque = deque(first)
    for step in range(len(first)):
        first_deque.rotate()
        if list(first_deque) == list(second):
            return step + 1

    return -1


if __name__ == "__main__":
    print(shifted_diff("eecoff", "coffee"))
    print(shifted_diff("Moose", "moose"))
    print(shifted_diff("isn't", "'tisn"))
    print(shifted_diff(" ", " "))
    print(shifted_diff("hoop", "pooh"))
    print(shifted_diff("  ", " "))

"""
def shifted_diff(first, second):
    return (second + second).find(first) if len(first) == len(second) else - 1


def shifted_diff(first, second):
    for shift in xrange(len(first)):
        if first==second:
            return shift
        first=first[-1]+first[:-1]
    return -1


def shifted_diff(first, second):
    for i in range(len(first)):
        if first == second[i:] + second[:i]:
            return i
    return -1

"""
