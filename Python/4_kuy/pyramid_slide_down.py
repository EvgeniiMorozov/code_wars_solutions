def longest_slide_down(pyramid: list[list]) -> int:
    for i in range(1, len(pyramid)):
        pyramid[i][0] += pyramid[i - 1][0]
        pyramid[i][i] += pyramid[i - 1][i - 1]
        for j in range(1, i):
            pyramid[i][j] += max(pyramid[i - 1][j], pyramid[i - 1][j - 1])
    return max(pyramid[-1])


if __name__ == "__main__":
    print(longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]))

"""
def longest_slide_down(p):
    res = p.pop()
    while p:
        tmp = p.pop()
        res = [tmp[i] + max(res[i],res[i+1])  for i in range(len(tmp))]
    return res.pop()
"""
