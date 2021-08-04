# https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python


def tickets(arr: list[int]) -> str:
    if arr[0] != 25:
        return "NO"
    cash = 0
    for i in arr:
        if i == 25:
            cash += 25
        elif i-25 > cash:
            return "NO"
        else:
            cash -= i - 25


if __name__ == "__main__":
    print(tickets([25, 25, 50]))
