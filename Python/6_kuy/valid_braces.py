def valid_braces(string: str) -> bool:
    stack = []
    opened = ("(", "[", "{")
    closed = (")", "]", "}")
    for el in string:
        if not stack and el in closed:
            return False

        if el in opened:
            stack.append(el)
        elif el == closed[0] and stack[-1] == opened[0]:
            stack.pop()
        elif el == closed[1] and stack[-1] == opened[1]:
            stack.pop()
        elif el == closed[2] and stack[-1] == opened[2]:
            stack.pop()
        else:
            return False

    return not stack


if __name__ == "__main__":
    print(valid_braces("([{}])"))
    print(valid_braces("{}()[]"))
    print(valid_braces("([}{])"))
    print(valid_braces("{}({})[]"))


"""
def valid_braces(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces:
            stack.append(character)
        elif not stack or braces[stack.pop()] != character:
            return False
    return not stack

def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''
"""
