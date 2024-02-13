# https://www.codewars.com/kata/5f631ed489e0e101a70c70a0

def contest(array: list[int]) -> list[int]:
    if len(array) == 1:
        return array
    res = [] if len(array) % 2 == 0 else [array[-1]]
    res.extend(max(array[i], array[i + 1]) for i in range(0, len(array)-1, 2))
    return res


def tourney(inp: list[int]) -> list[list[int]]:
    output = [inp, ]
    stages = len(inp) // 2 if len(inp) % 2 != 0 else int(len(inp) / 2 - 1)
    for _ in range(stages+1):
        stage = contest(inp)
        output.append(stage)
        inp = stage
        if len(inp) == 1:
            break

    return output


if __name__ == "__main__":
    print(tourney([9, 5, 4, 7, 6, 3, 8]))
    print(tourney([9, 5, 4, 7, 6, 3, 8, 2]))
    print(tourney([24, 21, 80, 27, 6, 2, 80, 59, 20, 6, 91]))


"""
def tourney(lst):
    out = [lst]
    while len(lst)>1:
        lst = [ lst[-1] ] * (len(lst)%2) + [ *map(max, lst[::2], lst[1::2])]
        out.append(lst)
    return out 
"""
