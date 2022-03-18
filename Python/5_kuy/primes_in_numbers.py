def primes(number) -> list:
    i = 2
    result = []
    while i ** 2 <= number:
        while number % i == 0:
            result.append(i)
            number = number / i
        i += 1
    if number > 1:
        result.append(int(number))
    return result


def prime_factors(number) -> str:
    factors = primes(number)
    if len(factors) == 1:
        return f"({number})"

    result = []
    for num in sorted(set(factors)):
        cnt = factors.count(num)
        result.append(f"({num})") if cnt == 1 else result.append(f"({num}**{cnt})")

    return "".join(result)


if __name__ == "__main__":
    print(primes(7775460))
    print(prime_factors(7775460))
    print(prime_factors(86240))

"""
def primeFactors(n):
    i, j, p = 2, 0, []
    while n > 1:
        while n % i == 0: n, j = n / i, j + 1
        if j > 0: p.append([i,j])
        i, j = i + 1, 0
    return ''.join('(%d' %q[0] + ('**%d' %q[1]) * (q[1] > 1) + ')' for q in p)
    

def primeFactors(n):
    i = 2
    r = ''
    while n != 1:
        k = 0
        while n%i == 0:
            n = n / i
            k += 1
        if k == 1:
            r = r + '(' + str(i) + ')'
        elif k == 0: pass
        else:
            r = r + '(' + str(i) + '**' + str(k) + ')'
        i += 1
        
    return r
"""
