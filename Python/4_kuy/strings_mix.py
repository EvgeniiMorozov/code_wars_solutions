# https://www.codewars.com/kata/5629db57620258aa9d000014

from string import ascii_lowercase


def mix(s1: str, s2: str) -> str:
    letters = {el for el in s1 if el in ascii_lowercase} | {el for el in s2 if el in ascii_lowercase}
    letters = sorted(list(letters))
    print(letters)
    result = []
    for letter in letters:
        count_1 = s1.count(letter)
        count_2 = s2.count(letter)
        if max(count_1, count_2) > 1:
            result.append((1, letter * count_1)) if count_1 > count_2 else result.append((2, letter * count_2))
    print(result)
    return ""


if __name__ == "__main__":
    print(mix("Are they here", "yes, they are here"))
