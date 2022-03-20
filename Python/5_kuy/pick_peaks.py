def pick_peaks(array: list) -> dict:
    if not array:
        return {"pos": [], "peaks": []}

    result = {"pos": [], "peaks": []}
    prev = [array[0], 0]
    condition = "down"
    for i, num in enumerate(array[1:]):
        if num > prev[0]:
            condition = "up"
            prev = [num, i + 1]
        elif num < prev[0]:
            if condition == "up":
                result["pos"].append(prev[1])
                result["peaks"].append(prev[0])
            condition = "down"
            prev = [num, i + 1]

    return result


if __name__ == "__main__":
    print(
        pick_peaks(
            [1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]
        )
    )
    print(
        pick_peaks(
            [
                18,
                18,
                10,
                -3,
                -4,
                15,
                15,
                -1,
                13,
                17,
                11,
                4,
                18,
                -4,
                19,
                4,
                18,
                10,
                -4,
                8,
                13,
                9,
                16,
                18,
                6,
                7,
            ]
        )
    )
    print(pick_peaks([]))
    print(pick_peaks([1, 1, 1, 1]))

"""
def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}


def pick_peaks(arr):
    peak, pos = [], []
    res = { "peaks":[], "pos":[] }

    for i in range(1, len(arr)) :
        if arr[i]>arr[i-1] :
            peak, pos = [arr[i]], [i]

        elif arr[i]<arr[i-1] :
            res["peaks"] += peak
            res["pos"] += pos
            peak, pos = [], []

    return res
"""
