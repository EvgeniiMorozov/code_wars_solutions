# https://www.codewars.com/kata/520b9d2ad5c005041100000f

def pig_it(text: str) -> str:
    arr = text.split(" ")
    result = []
    for el in arr:
        if el.isalpha():
            el = list(el)
            letter = el.pop(0)
            el = "".join(el)+letter+"ay"
        result.append(el)

    return " ".join(result)


if __name__ == "__main__":
    print(pig_it("Pig latin is cool"))
    print(pig_it("Hello world !"))

"""
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
"""
