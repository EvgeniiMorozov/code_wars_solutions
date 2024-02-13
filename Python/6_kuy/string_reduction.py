from collections import Counter


def solve(a: str, b: str) -> int:
    table_a = Counter(a)
    table_b = Counter(b)
    result = 0
    for el in table_a:
        if table_a[el] < table_b[el]:
            return 0
        result += table_a[el] - table_b[el] if el in table_b else table_a[el]
    return result


if __name__ == "__main__":
    print(solve("abdegfg", "ffdb"))
    print(solve("aabcdefg", "fbd"))
    print(solve("tvkmebckjmmscrr", "tvk"))

'''
from collections import Counter
def solve(a,b):
    return 0 if Counter(b) - Counter(a) else len(a) - len(b)

    
from collections import Counter
def solve(a,b):
    x = Counter(a)
    x.subtract(Counter(b))
    return (sum(x.values()),0)[any(_<0 for _ in x.values())]

def solve(a,b):
    for x in set(b):
        if a.count(x) >= b.count(x):
            continue
        else:
            return 0
    return len(a)-len(b)
'''
