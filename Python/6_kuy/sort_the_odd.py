# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/python

def sort_array(source_array: list[int]) -> list[int]:
    odd_list = [i for i in source_array if i % 2 != 0]
    odd_list.sort()
    return [i if i % 2 == 0 else odd_list.pop(0) for i in source_array]


if __name__ == "__main__":
    print(sort_array([5, 3, 2, 8, 1, 4]))

"""
def sort_array(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    return [next(odds) if i % 2 else i for i in source_array]
"""
