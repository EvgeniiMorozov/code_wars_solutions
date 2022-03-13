def calc(expr: str) -> int:
    valid_operations = ("+", "-", "*", "/")
    stack = []
    if not expr:
        return 0
    for e in expr.split():
        if e in valid_operations:
            num1, num2 = stack[-2], stack[-1]
            del stack[-2:]
            if e == "+":
                stack.append(num1 + num2)
            elif e == "-":
                stack.append(num1 - num2)
            elif e == "*":
                stack.append(num1 * num2)
            else:
                stack.append(num1 / num2)
        else:
            stack.append(eval(e))

    return stack[-1] if stack else 0

"""
import operator

def calc(expr):
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = [0]
    for token in expr.split(" "):
        if token in OPERATORS:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(OPERATORS[token](op1,op2))
        elif token:
            stack.append(float(token))
    return stack.pop()


import re

def calc(expr):
    if expr == "":
        return 0
    stack = []
    for elem in expr.split():
        if re.match(r"([0-9]+)", elem):
            try:
                stack.append(int(elem))
            except ValueError:
                stack.append(float(elem))
        if re.match(r"[\+\-\*\/]", elem):
            if elem == '+':
                stack.append(stack.pop(-2) + stack.pop(-1))
            if elem == '-':
                stack.append(stack.pop(-2) - stack.pop(-1))
            if elem == '*':
                stack.append(stack.pop(-2) * stack.pop(-1))
            if elem == '/':
                try:
                    stack.append(stack.pop(-2) / stack.pop(-1))
                except ZeroDivisionError:
                    print("Division by zero")
                    return 0
    return stack[-1]


operator = set(['+', '-', '*', '/'])

def calc(expr):
    stack = list()
    for c in expr.split():
        if c in operator :
            first = stack.pop()
            second = stack.pop()
            stack.append(str(eval(second + c + first)))
        else : stack.append(c)
    return eval(stack.pop()) if stack else 0


OPS = {'+': lambda x, y: y + x, '-': lambda x, y: y - x, '*': lambda x, y: y * x, '/': lambda x, y: y / x}

def calc(expr):
    if not expr:
        return 0
    stack = []
    [stack.append(*map(OPS[sign], [stack.pop()], [stack.pop()])) if sign in OPS else stack.append(float(sign)) for sign in expr.split(' ')]
    return stack[-1]

"""


if __name__ == "__main__":
    print(calc("4 2 /"))
    print(calc("5 1 2 + 4 * + 3 -"))
