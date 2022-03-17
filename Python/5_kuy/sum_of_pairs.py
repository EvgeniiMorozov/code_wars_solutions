def sum_pairs(ints: list[int], s: int):
    results = dict()
    short_ints = simplify(ints)
    for idx_a, a in enumerate(short_ints):
        for idx_b, b in enumerate(short_ints):
            if idx_a != idx_b:
                if a + b == s:
                    diff = abs(idx_a - idx_b)
                    if diff == 1:
                        return [a, b]

                    if diff not in results:
                        results[diff] = [a, b]

    return results[min(results)] if len(results) > 0 else None


def simplify(ints: list) -> list:
    result = []
    temp = -1
    for i in ints:
        if temp != i:
            temp = i
            result.append(i)

    return result


if __name__ == "__main__":
    print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
    print(sum_pairs([5, 9, 13, -3], 10))

"""
def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)
"""
