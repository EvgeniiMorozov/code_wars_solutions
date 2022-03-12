"""
def divisors(number: int) -> int:
    return sum([1] + [i for i in range(2, (number // 2) + 1) if number % i == 0])


def buddy(start: int, limit: int):
    for i in range(start, limit + 1):
        sum1 = divisors(i)
        sum_minus_one = divisors(sum1 - 1)

        if start > sum1 - 1 or i > sum1:
            continue

        if i == (sum_minus_one - 1):
            return [i, sum1 - 1]

    return "Nothing"


def div_sum(n):
    divs = set()
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            divs.add(x)
            divs.add(n // x)
    return sum(divs)

def buddy(start, limit):
    for n in range(start, limit+1):
        buddy = div_sum(n)

        if buddy > n and div_sum(buddy) == n:
            return [n, buddy]

    return "Nothing"

"""
from math import isqrt


def divisors(number: int) -> int:
    result: int = 1
    div: int = 1

    while True:
        for div in range(div+1, isqrt(number)+1):
            if not number % div:
                mul: int = 1
                while not number % div:
                    number //= div
                    mul = 1 + mul * div
                result *= mul
                break
        else:
            if number > 1:
                result *= 1 + number

            return result


def buddy(start: int, limit: int):
    def _s(n: int) -> int:
        return divisors(n) - n

    for n in range(start, limit+1):
        m = _s(n) - 1
        if m > n and _s(m) == n + 1:
            return [n, m]

    return "Nothing"


if __name__ == "__main__":
    print(buddy(10, 50))
    print(buddy(2177, 4357))
    print(buddy(57345, 90061))
    print(buddy(1071625, 1103735))
