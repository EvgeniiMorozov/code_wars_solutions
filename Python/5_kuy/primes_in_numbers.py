def prime_factors(number: int) -> str:
    result = ""
    for i in range(2, number+1):
        f = 0
        while number % i == 0:
            f += 1
            number /= i
        if f:
            result += "(" + (str(i) + "**" + str(f)) if f > 1 else (str(i)) + ")"
        else:
            result += ""

    return result if result else "(" + str(number) + ")"


if __name__ == "__main__":
    print(prime_factors(7775460))
    print(prime_factors(86240))
