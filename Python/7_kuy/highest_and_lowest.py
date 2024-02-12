def high_and_low(numbers: str) -> str:
    nums = [int(num) for num in numbers.split(" ")]
    return f"{max(nums)} {min(nums)}"


if __name__ == "__main__":
    print(high_and_low("1 2 -3 4 5"))
    print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
