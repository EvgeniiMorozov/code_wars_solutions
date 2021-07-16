# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def snail(array: list[list]) -> list:
    result = []
    while array:
        result += array[0]
        del array[0]

        if array:
            for i in array:
                result += [i[-1]]
                del i[-1]

            if array[-1]:
                result += array[-1][::-1]
                del array[-1]

            for i in reversed(array):
                result += [i[0]]
                del i[0]

    return result


"""
def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out

import itertools

def transpose_and_yield_top(arr):
    while arr:
        yield arr[0]
        arr = list(reversed(list(zip(*arr[1:]))))
"""

if __name__ == "__main__":
    array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # array = [[4,5,6], [7,8,9]]
    # print(list(itertools.chain(*transpose_and_yield_top(array))))
    print(snail(array))
