def order_weight(strng: str) -> str:
    weights_conv = [sum(int(i) for i in list(elem)) for elem in strng.split(" ")]
    return " ".join([x for _, x in sorted(zip(weights_conv, strng.split(" ")))])


if __name__ == "__main__":
    print(order_weight("103 123 4444 99 2000"))

"""
def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))
"""
