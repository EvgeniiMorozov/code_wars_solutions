def make_readable(seconds: int) -> str:
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


if __name__ == "__main__":
    print(make_readable(0))
    print(make_readable(5))
    print(make_readable(60))
    print(make_readable(86399))
    print(make_readable(359999))

"""
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
"""
