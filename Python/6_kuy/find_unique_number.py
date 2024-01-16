def find_uniq(arr: list):
    return min(arr) if arr.count(min(arr)) == 1 else max(arr)


if __name__ == "__main__":
    arrays = [[1, 1, 1, 2, 1, 1], [0, 0, 0.55, 0, 0]]
    for arr in arrays:
        print(find_uniq(arr))

    """
    def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
    """
