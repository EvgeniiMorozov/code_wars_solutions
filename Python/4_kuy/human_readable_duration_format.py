# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python
def format_duration(seconds: int) -> str:
    if seconds == 0:
        return "now"

    result: list = []
    rest = seconds
    for divisor, name in zip([60, 60, 24, 365, float("inf")], ["second", "minute", "hour", "day", "year"]):
        value = int(rest % divisor)
        rest = (rest - value) // divisor
        if value:
            string = f"{value} {name}"
            if value > 1:
                string += "s"
            result.append(string)

    result.reverse()

    if len(result) > 1:
        return ", ".join(result[:-1]) + " and " + result[-1]

    return result[-1]


if __name__ == "__main__":
    secs = [1, 62, 120, 3600, 3662, 3661]
    for sec in secs:
        print(format_duration(sec))
