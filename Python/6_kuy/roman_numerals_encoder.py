# https://www.codewars.com/kata/51b62bf6a9c58071c600001b


def solution(num: int) -> str:
    arab_nums = [1000, 990, 900, 500, 490, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_nums = ["M", "CMXC", "CM", "D", "CDXC", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ""
    i = 0
    while num > 0 or len(arab_nums) == (i - 1):
        while (num - arab_nums[i]) >= 0:
            num -= arab_nums[i]
            result += roman_nums[i]
        i += 1
    return result


if __name__ == "__main__":
    nums = [984, 14, 21, 1000, 1889, 1989]
    for num in nums:
        print(solution(num))
