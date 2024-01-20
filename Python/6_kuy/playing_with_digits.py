def dig_pow(n: int, p: int) -> int:
    arr = [int(el)**(p+i) for i, el in enumerate(str(n))]
    sum_arr = sum(arr)
    k, r = divmod(sum_arr, n)
    return k if r == 0 else -1


if __name__ == "__main__":
    # print(dig_pow(89, 1))
    # print(dig_pow(92, 1))
    print(dig_pow(46288, 3))
