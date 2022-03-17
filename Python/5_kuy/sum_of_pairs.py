def sum_pairs(ints: list[int], s: int):
    arr = []
    for i in range(len(ints)):
        term = s - ints[i]
        if term == 0:
            continue
        if term not in ints:
            continue

        idx = ints.index(term)
        arr.append((i, idx, abs(idx - i)))
    print(arr)

    return None


if __name__ == "__main__":
    print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
    print(sum_pairs([5, 9, 13, -3], 10))
