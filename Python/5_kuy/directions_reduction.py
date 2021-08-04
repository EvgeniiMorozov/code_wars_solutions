# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python


def dirReduc(arr: list) -> list:
    dir = {"NORTH":"SOUTH","SOUTH":"NORTH","WEST":"EAST","EAST":"WEST",}
    result = []
    for step in arr:
        if result and dir[step] == result[-1]:
            result.pop()
        else:
            result.append(step)

    return result


if __name__ == "__main__":
    print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
    print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))
