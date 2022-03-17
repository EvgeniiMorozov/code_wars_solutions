def ips_between(start: str, end: str) -> int:
    start = [int(el) for el in start.split(".")]
    end = [int(el) for el in end.split(".")]
    diff = list(map(lambda x: x[1] - x[0], zip(start, end)))
    total = list(map(lambda x: x[1] * x[0], zip(diff, [256**3, 256**2, 256, 1])))
    return sum(total)


if __name__ == "__main__":
    print(ips_between("10.0.0.0", "10.0.0.50"))
    print(ips_between("10.0.0.0", "10.0.1.0"))
    print(ips_between("20.0.0.10", "20.0.1.0"))

"""
from ipaddress import ip_address

def ips_between(start, end):
    return int(ip_address(end)) - int(ip_address(start))


def ips_between(start, end):
    a = sum([int(e)*256**(3-i) for i, e in enumerate(start.split('.'))])
    b = sum([int(e)*256**(3-i) for i, e in enumerate(end.split('.'))])
    return abs(a-b)
"""
