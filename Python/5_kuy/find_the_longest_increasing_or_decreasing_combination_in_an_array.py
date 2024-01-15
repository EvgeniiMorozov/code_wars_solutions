# https://www.codewars.com/kata/5715508de1bf8174c1001832
def longest_comb(arr: list, command: str) -> list:
    if command in ["> >", ">>"]:
        return [arr[0]] + [arr[i] for i in range(1, len(arr)) if arr[i] < arr[i - 1]]
    else:
        return [arr[0]] + [arr[i] for i in range(1, len(arr)) if arr[i] > arr[i - 1]]


if __name__ == "__main__":
    print(longest_comb([-1, 3, -34, 18, -55, 60, 118, -64], '< <'))
    print(longest_comb([-1, 3, -34, 18, -55, 60, 118, -64], '> >'))
