from re import findall


def camelize(string: str) -> str:
    array = findall(r"[a-zA-Z0-9]+", string)

    return "".join(el.capitalize() for el in array)


if __name__ == "__main__":
    print(camelize("your-NaMe-here"))
    print(camelize("example name"))
    print(camelize("testing ABC"))


"""

import re

def camelize(s):
    return "".join([w.capitalize() for w in re.split("\W|_", s)])

"""
