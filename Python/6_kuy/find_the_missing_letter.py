# https://www.codewars.com/kata/5839edaa6754d6fec10000a2

def find_missing_letter(chars: list[str]) -> str:
    for i in range(len(chars)):
        if ord(chars[i]) + 1 != ord(chars[i + 1]):
            return chr(ord(chars[i]) + 1)


if __name__ == "__main__":
    print(find_missing_letter(["a", "b", "c", "d", "f"]))

"""
def find_missing_letter(chars):
    return [chr(n) for n in range(ord(chars[0]),ord(chars[-1])+1) if n not in [ord(c) for c in chars]][0]
"""
