# https://www.codewars.com/kata/530e15517bc88ac656000716
def rot13(message: str) -> str:
    cipher_table = {}
    for ch in range(26):
        cipher_table[chr(ch + ord("A"))] = chr(((ch + 13) % 26) + ord("A"))
        cipher_table[chr(ch + ord("a"))] = chr(((ch + 13) % 26) + ord("a"))

    return "".join(cipher_table.get(ch, ch) for ch in message)


if __name__ == "__main__":
    print(rot13("test"))
    print(rot13("Test"))
