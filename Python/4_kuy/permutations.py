# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python


def permutations(string):
    result = set([string, string[::-1]])

    if len(string) > 2:
        for i, char in enumerate(string):
            for s in permutations(string[:i] + string[i+1:]):
                result.add(char + s)

    return list(result)


if __name__ == "__main__":
    print(permutations("aabb"))
