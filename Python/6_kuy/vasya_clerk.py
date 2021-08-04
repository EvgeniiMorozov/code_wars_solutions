# https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python


# def tickets(arr: list[int]) -> str:
#     if arr[0] != 25:
#         return "NO"
#     cash = 0
#     for i in arr:
#         if i == 25:
#             cash += 25
#         elif i-25 > cash:
#             return "NO"
#         else:
#             cash -= i - 25
#     return "YES"


def tickets(people):
    cash_25 = cash_50 = 0
    for bill in people:
        if bill == 25:
            cash_25 += 1
            continue
        if bill == 50:
            if cash_25 >= 1:
                cash_25 -= 1
                cash_50 += 1
                continue
            else:
                return "NO"
        if bill == 100:
            if cash_50 >= 1 and cash_25 >= 1:
                cash_50 -= 1
                cash_25 -= 1
                continue
            elif cash_25 >= 3:
                cash_25 -= 3
                continue
            else:
                return "NO"
    return "YES"


if __name__ == "__main__":
    print(tickets([25, 25, 50]))
