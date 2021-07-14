# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

import re


def increment_string(string: str) -> str:
    if string == "":
        return "1"

    if string.isalpha():
        return string + "1"

    nums = re.findall(r"^[a-z]*(0*\d*)", string, flags=re.IGNORECASE)[0]
    alpha = re.findall(r"^([a-z]*)0*\d*", string, flags=re.IGNORECASE)[0]

    nums_result = str(int(nums) + 1)

    if len(nums) < len(nums_result):
        while len(nums) != len(nums_result):
            nums_result.split().extend(0, "0")
        nums_result = "".join(nums_result)

    return alpha + nums_result


if __name__ == "__main__":
    strings = ["foo", "foobar0099090", "foo00", "foo099"]
    for string in strings:
        print(increment_string(string))
