import re


def decipher_this(s: str) -> str:
    words_list = s.split(" ")
    result = []
    for word in words_list:
        if word.isnumeric():
            result.append(chr(int(word)))
        else:
            lst = re.findall(r"(\d+)(\w+)", word)
            digits, chars = lst[0]
            if len(chars) > 3:
                tmp = list(chars)
                second, last = tmp.pop(0), tmp.pop()
                chars = last+"".join(tmp)+second
            else:
                chars = chars[::-1]
            result.append(chr(int(digits)) + chars)
    return " ".join(result)


if __name__ == "__main__":
    print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"))
    print(decipher_this("72olle 103doo 100ya"))
    print(decipher_this("84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"))
