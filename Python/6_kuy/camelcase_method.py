# https://www.codewars.com/kata/587731fda577b3d1b0001196


def camel_case(s: str) -> str:
    return "".join([word[0].upper() + word[1:] for word in s.split()])
