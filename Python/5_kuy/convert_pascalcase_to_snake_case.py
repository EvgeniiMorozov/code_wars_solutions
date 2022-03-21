from re import findall


def to_underscore(string) -> str:
    if not isinstance(string, str):
        return str(string)

    array = findall(r"([A-Z0-9]{1}[a-z0-9]+)", string)
    return "_".join(el.lower() for el in array)


if __name__ == "__main__":
    print(to_underscore("TestController"))
    print(to_underscore("MoviesAndBooks"))
    print(to_underscore("App7Test"))
    print(to_underscore(1))

"""
import re

def to_underscore(string):
    return re.sub(r'(.)([A-Z])', r'\1_\2', str(string)).lower()


def to_underscore(string):
    return ''.join('_'+c.lower() if c.isupper() else c for c in str(string)).lstrip('_')
"""
