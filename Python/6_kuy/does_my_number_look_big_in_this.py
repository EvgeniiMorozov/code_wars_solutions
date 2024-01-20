def narcissistic(value: int) -> bool:
    return value == sum(int(el)**len(str(value)) for el in str(value))


if __name__ == "___main__":
    print(narcissistic(7))
    print(narcissistic(371))
    print(narcissistic(122))
    print(narcissistic(4887))
