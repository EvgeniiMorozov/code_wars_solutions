# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python


def permutations(string):
    result = set([string, string[::-1]])

    if len(string) > 2:
        for i, char in enumerate(string):
            for s in permutations(string[:i] + string[i+1:]):
                result.add(char + s)

    return list(result)


"""
import itertools

def permutations(string):
    return list("".join(p) for p in set(itertools.permutations(string)))


def permutations(s):
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [s]
    else:
        return set(s[i]+p for i in range(len(s)) for p in permutations(s[:i] + s[i+1:]))
"""


if __name__ == "__main__":
    print(permutations("aabb"))
