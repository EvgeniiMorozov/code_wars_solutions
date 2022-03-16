def closest(string: str) -> list:
    if not string:
        return []

    strings = (string.rstrip()).split(" ")
    array = [
        [sum(int(j) for j in list(strings[i])), i, int(strings[i])]
        for i in range(len(strings))
    ]
    array = sorted(array, key=lambda el: el[0])

    return array[:2]


if __name__ == "__main__":
    print(closest("103 123 4444 99 2000 "))
    print(closest(""))
