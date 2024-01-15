# https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python

def multiplication_table(size: int) -> list:
    return [[m*n for m in range(1, size+1)] for n in range(1, size+1)]


if __name__ == "__main__":
    print(multiplication_table(3))
    print(multiplication_table(1))
