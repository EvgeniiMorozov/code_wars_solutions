def sort_nested_list(A):
    vals = []
    for sub_lst in A:
        for lst in sub_lst:
            vals += lst
    vals = sorted(vals)
    for i, sub_lst in enumerate(A):
        for j, lst in enumerate(sub_lst):
            for k in range(len(lst)):
                A[i][j][k] = vals.pop(0)
    return A


if __name__ == "__main__":
    print(sort_nested_list([[[82, 87], [47, 44]], [[70, 94], [40, 64]]]))
    print(sort_nested_list([[[29, 32], [82, 61], [75, 91]], [[69, 99], [74, 23], [70, 97]]]))
