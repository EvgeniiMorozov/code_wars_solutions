# https://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/python


# def anagrams(word: str, words: list[str]) -> list:
#     result = []
#     for chunk in words:

#         if len(word) != len(chunk):
#             continue

#         temp = chunk.split()
#         for i in word.split():
#             try:
#                 temp.remove(i)
#             except ValueError:
#                 continue

#         if len(temp) == 0:
#             result.append(chunk)

#     return result

from collections import Counter


def anagrams(word, words):
    template = Counter(word)
    return [w for w in words if Counter(w) == template]


if __name__ == "__main__":
    array = [
        ["abba", ["aabb", "abcd", "bbaa", "dada"]],
        ["racer", ["crazer", "carer", "racar", "caers", "racer"]],
        ["laser", ["lazing", "lazy", "lacer"]],
    ]
    for arr in array:
        print(anagrams(*arr))
