def closest(s: str) -> list:
    wght = sorted(
        [[sum(int(c) for c in n), i, int(n)] for i, n in enumerate(s.split())],
        key=lambda k: (k[0], k[1]),
    )
    diff = [abs(a[0] - b[0]) for a, b in zip(wght, wght[1:])]
    return (
        [wght[diff.index(min(diff))], wght[diff.index(min(diff)) + 1]] if wght else []
    )


if __name__ == "__main__":
    print(closest("103 123 4444 99 2000 "))
    print(closest(""))

"""
def closest(strng):
    if (strng == ""): return []
    nums, l, i = strng.split(), [], 0
    for n in nums:
        s = sum(list(int(i) for i in n))
        l += [[s, i, int(n)]]
        i += 1
    l.sort()
    valmin, argmin = min((l[i][0] - l[i - 1][0], i) for i in range(1, len(l)))
    return [l[argmin - 1], l[argmin]]
"""
