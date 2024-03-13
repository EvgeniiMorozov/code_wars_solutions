# https://www.codewars.com/kata/52c31f8e6605bcc646000082


def two_sum(numbers: list[int], target: int):
    for i in range(len(numbers)):
        num = target - numbers[i]
        arr = numbers[:i] + numbers[i + 1:]
        if num in arr:
            idx = arr.index(num)
            return (idx, i) if idx < i else (i, idx + 1)


if __name__ == "__main__":
    print(two_sum([1, 2, 3], 4))
    print(two_sum([1234, 5678, 9012], 14690))
    print(two_sum([2, 2, 3], 4))

    """
    def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]
    """
