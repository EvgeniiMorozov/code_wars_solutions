def max_sequence(arr):
    maximum = total = 0
    for a in arr:
        total = max(0, total + a)
        if total > maximum:
            maximum = total
    return maximum


if __name__ == "__main__":
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
