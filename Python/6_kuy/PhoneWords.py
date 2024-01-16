def phone_words(string_of_nums: str) -> str:
    if not string_of_nums:
        return ""

    phone_symbols = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    symbols = []
    buff = string_of_nums[0]
    for i in range(1, len(string_of_nums)):
        if string_of_nums[i] == buff[-1]:
            buff += string_of_nums[i]
        else:
            symbols.append(buff)
            buff = string_of_nums[i]
        if i == len(string_of_nums) - 1:
            symbols.append(buff)

    result = ""
    for symbol in symbols:
        key = symbol[0]
        if key == "0":
            result += " " * len(symbol)
        elif key == "1":
            result += ""
        else:
            if len(symbol) <= len(phone_symbols[key]):
                result += phone_symbols[key][len(symbol) - 1]
            else:
                m, n = divmod(len(symbol), len(phone_symbols[key]))
                result += phone_symbols[key][-1]*m + phone_symbols[key][n-1] if n != 0 else phone_symbols[key][-1]*m

    return result


if __name__ == "__main__":
    # print(phone_words("22266631339277717777"))
    print(phone_words("443355555566604466690277733099966688"))
    # oisq  rtflvhovsgavul
    # oisqq  rtflvhovsgavuul
    # print(phone_words("6664447777770077783335558881446668887777412888885551"))

"""
import re
def phone_words(str):
    ansd = {'0':' ','2':'a','22':'b','222':'c','3':'d','33':'e','333':'f',\
           '4':'g','44':'h','444':'i','5':'j','55':'k','555':'l','6':'m',\
           '66':'n','666':'o','7':'p','77':'q','777':'r','7777':'s','8':'t','88':'u',\
           '888':'v','9':'w','99':'x','999':'y','9999':'z'}
    ans=''
    for i in re.findall('0|2{1,3}|3{1,3}|4{1,3}|5{1,3}|6{1,3}|7{1,4}|8{1,3}|9{1,4}',str):
        ans+=ansd[i]
    return ans
    

from itertools import groupby

KEYBOARD = {
    "1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz", "0": " "
}

def phone_words(str):
    ans = []
    for digit, sequence in filter(lambda x: x[0] != "1", groupby(str)):
        q, r = divmod(len(list(sequence)), len(KEYBOARD[digit]))
        if q: ans.append(KEYBOARD[digit][-1] * q)
        if r: ans.append(KEYBOARD[digit][r - 1])
    return "".join(ans)

"""
