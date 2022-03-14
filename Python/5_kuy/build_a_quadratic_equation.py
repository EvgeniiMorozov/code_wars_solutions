"""
def quadratic_builder(expression: str) -> str:
    nums = []
    for i in range(len(expression)):
        if expression[i].isdigit():
            if expression[i - 1] == "-":
                nums.append(int(expression[i]) * -1)
            else:
                nums.append(int(expression[i]))
        elif expression[i].isalpha():
            letter = expression[i]
            if expression[i - 1] == "-":
                nums.append(-1)
            if expression[i - 1] == "(":
                nums.append(1)

    multipliers = [nums[0] * nums[2], nums[0] * nums[3] + nums[1] * nums[2], nums[1] * nums[3]]

    chunks = []
    for i, num in enumerate(multipliers, start=1):
        if num == 0:
            chunks.append("")
        elif num == [1, -1]:
            if i == 1:
                chunks.append(f"{letter}^2") if num == 1 else chunks.append(f"-{letter}^2")
            elif i == 2:
                chunks.append(f"+{letter}") if num == 1 else chunks.append(f"-{letter}")
            elif i == 3:
                chunks.append(str(num))
        elif num > 1 or num < -1:
            if i == 1:
                chunks.append(f"{num}{letter}^2") if num > 1 else chunks.append(f"{num}{letter}^2")
            elif i == 2:
                chunks.append(f"+{num}{letter}") if num > 1 else chunks.append(f"{num}{letter}")
            elif i == 3:
                chunks.append(f"+{num}") if num > 1 else chunks.append(f"{num}")

    return "".join(chunks)
"""
from re import findall as re_findall


def quadratic_builder(expression: str) -> str:
    pattern = r"^\((-?[1-9]?)([a-z])([+|-])([1-9])\)\((-?[1-9]?)([a-z])([+|-])([1-9])\)"
    arr = re_findall(pattern, expression)
    expr_tuple = sum(expression, ())
    # [('', 'x', '+', '2', '', 'x', '+', '3')]
    m = expr_tuple





if __name__ == "__main__":
    print(quadratic_builder("(x+2)(x+3)"))
    print(quadratic_builder("(x-2)(x+7)"))
    print(quadratic_builder("(3y+2)(y+5)"))
    print(quadratic_builder("(-h-7)(4h+3)"))
