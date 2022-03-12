from functools import reduce


def ip_to_num(ip: str) -> int:
    return reduce(lambda a, b: (a << 8) + b, map(int, ip.split(".")), 0)


def num_to_ip(num: int) -> str:
    return '.'.join([str(num >> (i << 3) & 0xFF) for i in range(4)[::-1]])


if __name__ == "__main__":
    pass

"""

def ip_to_num(ip):
    nums = list(map(int, ip.split('.')))
    return (nums[0] << 24) + (nums[1] << 16) + (nums[2] << 8) + nums[3]

def num_to_ip(num):
    return f"{num >> 24 & 255}.{num >> 16 & 255}.{num >> 8 & 255}.{num & 255}"


def ip_to_num(ip):
    return int("".join(f'{int(i):b}'.zfill(8) for i in ip.split(".")),2)

def num_to_ip(num):
    return  ".".join(str(int(i[::-1],2)) for i in [f'{num:b}'[::-1][i:i+8] for i in range(0,len(f'{num:b}'),8)][::-1])


ip_to_num = lambda ip : int(''.join(bin(int(e))[2:].zfill(8) for e in ip.split('.')), 2)
num_to_ip = lambda num: '.'.join(str(int(bin(num)[2:].zfill(32)[i:i+8], 2)) for i in (0, 8, 16, 24))

"""
