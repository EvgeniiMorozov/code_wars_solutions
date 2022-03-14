# https://www.codewars.com/kata/52f3bb2095d6bfeac2002196/train/python
from re import match


def valid_word(seq: list, word: str) -> bool:
    pattern = (f"^(?:{'|'.join(seq)})+$")
    return bool(match(pattern, word))


if __name__ == "__main__":
    print(valid_word(['code', 'wars'], 'codewars'))
    print(valid_word(['wars', 'code'], 'codewars'))
    print(valid_word(['code', 'wars'], 'codecodewars'))
    print(valid_word(['code', 'wars'], 'codewar'))
    print(valid_word(['Star', 'Code', 'Wars'], 'StarCodeWars'))
    print(valid_word(['a', 'b', 'c', 'd', 'e', 'f'], 'abcdef'))
    print(valid_word(['a', 'b', 'c', 'd', 'e', 'f'], 'abcdefg'))
    print(valid_word(['ab', 'a', 'bc'], 'abc'))
    print(valid_word(['ab', 'bc'], 'abc'))


"""

def valid_word(seq, word):
    return not word or any(valid_word(seq,word[len(x):]) for x in seq if word.startswith(x))


def valid_word(S, word):
    prS = set()
    nxS = set(word.replace(w, '') for w in S)
    while nxS!=prS:
        prS = nxS
        nxS = set(wrd.replace(w, '') for w in S for wrd in nxS)
    return '' in nxS


import re
def valid_word(seq, word):
    regex = '^(' + '|'.join(seq) + ')+$'
    if re.match(regex, word):
        return True
    return False

"""
