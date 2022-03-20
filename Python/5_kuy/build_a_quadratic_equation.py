def parse(expr: str) -> dict:
    coeff = []
    prev = "("
    result = dict()
    for i in range(1, len(expr)):
        if expr[i].isdigit():
            if prev == "-":
                coeff.append(-int(expr[i]))
            elif prev.isdigit():
                coeff.append(int(str(coeff.pop()) + expr[i]))
            else:
                coeff.append(int(expr[i]))
        if expr[i].isalpha():
            if not result.get("letter"):
                result["letter"] = expr[i]
            if prev == "(":
                coeff.append(1)
            elif prev == "-":
                coeff.append(-1)
        prev = expr[i]
    result.update({"coeff": coeff})
    return result


def quadratic_builder(expression: str) -> str:
    data = parse(expression)
    m, n, p, q = data["coeff"]
    letter = data["letter"]
    a = m * p
    b = m * q + n * p
    c = n * q
    if not a:
        first = ""
    elif abs(a) == 1:
        first = f"{letter}^2" if a > 0 else f"-{letter}^2"
    else:
        first = f"{a}{letter}^2"
    if not b:
        second = ""
    elif abs(b) == 1:
        second = f"+{letter}" if b > 0 else f"-{letter}"
    else:
        second = f"+{b}{letter}" if b > 0 else f"{b}{letter}"
    third = ""
    if c:
        third = f"+{c}" if c > 0 else f"{c}"

    return first + second + third


if __name__ == "__main__":
    # print(parse("(-h-7)(4h+3)"))
    print(parse("(g-2)(-33g-66)"))
    print(quadratic_builder("(x+2)(x+3)"))
    print(quadratic_builder("(x-2)(x+7)"))
    print(quadratic_builder("(3y+2)(y+5)"))
    print(quadratic_builder("(-h-7)(4h+3)"))
    print(quadratic_builder("(g-2)(-33g-66)"))

"""
import re

def quadratic_builder(expression):
    # replace -x with -1x in the expression
    expression = re.sub("-([a-z])", r"-1\1", expression)

    # extract constants and variable name
    m, x, n, p, _, q = re.findall("""
        \(          # opening bracket
        (-?\d*)     # constant (m)
        (\D)        # variable (x)
        ([+-]\d*)   # constant (n)
        \)          # closing bracket
        \(          # opening bracket
        (-?\d*)     # constant (p)
        (\D)        # variable (x)
        ([+-]\d*)   # constant (q)
        \)          # closing bracket
        """, expression, flags=re.VERBOSE).pop()
    m, n, p, q = map(int, [m or 1, n, p or 1, q])

    # calculate constants of the result
    a, b, c = m * p, m * q + n * p, n * q

    # construct output
    A = f"{a}{x}^2"     if a != 0 else ""
    B = f"{b:+}{x}"     if b != 0 else ""
    C = f"{c:+}"        if c != 0 else ""

    # remove 1s
    result = re.sub(r"(\b|\+|-)1" + x, r"\1" + x, A + B + C )

    return result


import re

def quadratic_builder(_):
    a,b,c,d=map(lambda _:int((1,(-1,_)[_>'-'])[bool(_)]),re.findall(r'\((-?\d*)\w\+?(-?\d+)\)\((-?\d*)\w\+?(-?\d+)\)',_)[0])
    return re.sub('(^|(?<=\D))1(?=\D|$)|(\D|^)0(\w|$)','',f"{a*c}{(z:=re.search('(?i)[a-z]',_)[0])}^2+{a*d+b*c}{z}+{b*d}".replace('+-','-'))


import re

def quadratic_builder(s):
    (a,x,b),(c,_,d) = re.findall(r'\((-?\d*)(\D)\+?(-?\d+)\)',s)
    a,b,c,d = (int(v or 1 if v!='-' else -1) for v in (a,b,c,d))
    s = '+'.join(str(v)+p for v,p in zip( (a*c, a*d+b*c, b*d), (f'{x}^2',x,'') ) if v)
    return re.sub(r'\+(?=-)|(?<!\d)1(?=[a-z])', '', s)
"""
