# https://www.codewars.com/kata/5629db57620258aa9d000014

from string import ascii_lowercase


def mix(s1: str, s2: str) -> str:
    letters = {el for el in s1 if el in ascii_lowercase} | {el for el in s2 if el in ascii_lowercase}
    result = []
    for letter in letters:
        n1, n2 = s1.count(letter), s2.count(letter)
        if max(n1, n2) > 1:
            if n1 > n2:
                result.append("1:" + letter * n1)
            elif n1 < n2:
                result.append("2:" + letter * n2)
            else:
                result.append("=:" + letter * n1)

    return "/".join(sorted(result, key=lambda s: (-len(s), s)))


"""

def mix(s1, s2):
hist = {}
for ch in "abcdefghijklmnopqrstuvwxyz":
    val1, val2 = s1.count(ch), s2.count(ch)
    if max(val1, val2) > 1:
        which = "1" if val1 > val2 else "2" if val2 > val1 else "="
        hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))

def mix(s1, s2):
    c1 = {l: s1.count(l) for l in s1 if l.islower() and s1.count(l) > 1}
    c2 = {l: s2.count(l) for l in s2 if l.islower() and s2.count(l) > 1}
    r = []
    for c in set(c1.keys() + c2.keys()):
        n1, n2 = c1.get(c, 0), c2.get(c, 0)
        r.append(('1', c, n1) if n1 > n2 else
                 ('2', c, n2) if n2 > n1 else
                 ('=', c, n1))

    rs = ['{}:{}'.format(i, c * n) for i, c, n in r]
    return '/'.join(sorted(rs, key=lambda s: (-len(s), s)))

"""

if __name__ == "__main__":
    print(mix("Are they here", "yes, they are here"))
