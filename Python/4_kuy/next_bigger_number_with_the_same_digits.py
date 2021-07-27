# https://www.codewars.com/kata/55983863da40caa2c900004e/train/python
from itertools import permutations


def next_bigger(num: int) -> int:
    nums = sorted({int("".join(chunk)) for chunk in permutations(str(num))})
    try:
        return nums[nums.index(num)+1]
    except:
        return -1


"""

def next_bigger(num: int) -> int:
    if num < 12:
        return -1
    nums = sorted({int("".join(chunk)) for chunk in permutations(str(num))})
    if nums[-1] == num:
        return -1
    return nums[nums.index(num)+1]

"""


if __name__ == "__main__":
    print(next_bigger(414))
