# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python
from itertools import product


def get_pins(observed: str) -> list[str]:
    template = ["08", "124", "1235", "236", "1457", "24568", "3569", "478", "05789", "689"]
    return ["".join(chunk) for chunk in product(*(template[int(i)] for i in observed))]


if __name__ == "__main__":
    print(get_pins("369"))