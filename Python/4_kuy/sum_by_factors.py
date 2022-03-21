def prime_factors(number) -> list:
    number = abs(number)
    i = 2
    result = []
    while i ** 2 <= number:
        while number % i == 0:
            result.append(i)
            number /= i
        i += 1
    if number > 1:
        result.append(int(number))
    return result


def sum_for_list(lst: list):
    if not lst:
        return []

    factors = []
    for num in lst:
        factors = list(set(factors).union(prime_factors(num)))

    result = []
    for i in range(len(factors)):
        msum = sum(item for item in lst if not item % factors[i])
        result.append([factors[i], msum])

    return sorted(result, key=lambda el: el[0])


if __name__ == "__main__":
    print(sum_for_list([12, 15]))
    print(sum_for_list([15, 21, 24, 30, 45]))
