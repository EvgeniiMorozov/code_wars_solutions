# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

import re

def increment_string(string: str) -> str:
    if string == "":
        return "1"

    nums = re.findall(r"^[a-z]*0*(\d*)", string, flags=re.IGNORECASE)[0]
    alpha = re.findall(r"^([a-z]*0*)\d*", string, flags=re.IGNORECASE)[0]

    if len(nums) == 0:
        if alpha[-1] == "0":
            alpha = alpha[:-1]
        nums = 0

    return alpha + str(int(nums)+1)


if __name__ == "__main__":
    strings = ["foo", "foobar0099090", "foo00", "foo099"]
    for string in strings:
        print(increment_string(string))
