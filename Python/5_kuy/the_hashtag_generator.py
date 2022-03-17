from re import findall


def generate_hashtag(string: str):
    if not string:
        return False

    arr = findall(r"([a-zA-Z]+)", string)
    result = "#" + "".join(el.capitalize() for el in arr)
    return result if len(result) <= 140 else False


if __name__ == "__main__":
    print(generate_hashtag("    Hello     World   "))

"""
def generate_hashtag(s):
    output = "#"

    for word in s.split():
        output += word.capitalize()

    return False if (len(s) == 0 or len(output) > 140) else output
"""
