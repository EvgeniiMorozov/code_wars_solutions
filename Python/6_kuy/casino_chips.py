def solve(arr: list) -> int:
    arr = sorted(arr)
    return arr[0] + arr[1] if arr[0] + arr[1] <= arr[2] else sum(arr) // 2


if __name__ == "__main__":
    print(solve([1, 1, 1]))
    print(solve([1, 2, 1]))
    print(solve([4, 1, 1]))
    print(solve([8, 2, 8]))
    print(solve([7, 4, 10]))
    print(solve([12, 12, 12]))

"""

def solve(xs):
    x, y, z = sorted(xs)
    return min(x + y, (x + y + z) // 2)

"""
