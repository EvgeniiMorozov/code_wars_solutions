def func(word: str):
    length2 = len(word) // 2
    if len(word) % 2 == 0:
        return word[:length2][::-1] + word[length2:][::-1]
    return word[:length2][::-1] + word[length2] + word[length2+1:][::-1]


def inside_out(string: str) -> str:
    result = [func(elem) for elem in string.split(" ")]
    return " ".join(result)


if __name__ == "__main__":
    # print(func("climbing"))
    # print(func("volcano"))
    print(inside_out('man i need a taxi up to ubud'))
    print(inside_out('what time are we climbing up the volcano'))
    print(inside_out('take me to semynak'))

"""
import re

def inside_out(s):
    return re.sub(r'\S+', lambda m: inside_out_word(m.group()), s)

def inside_out_word(s):
    i, j = len(s) // 2, (len(s) + 1) // 2
    return s[:i][::-1] + s[i:j] + s[j:][::-1]
"""
