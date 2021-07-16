# https://www.codewars.com/kata/529bf0e9bdf7657179000008

def valid_solution(board: list[list]) -> bool:
    template = {i for i in range(1, 10)}

    for row in board:
        if set(row) != template:
            return False

    for j in range(len(board[0])):
        column = [board[i][j] for i in range(len(board))]
        if set(column) != template:
            return False

    for left_shift in range(0, 9, 3):
        for down_shift in range(0, 9, 3):
            square = {
                board[i][j]
                for i in range(left_shift, 3+left_shift)
                for j in range(down_shift, 3+down_shift)
            }
            if set(square) != template:
                return False

    return True


if __name__ == "__main__":
    arrays = [
        [[5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]],

        [[5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 0, 3, 4, 9],
        [1, 0, 0, 3, 4, 2, 5, 6, 0],
        [8, 5, 9, 7, 6, 1, 0, 2, 0],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 0, 1, 5, 3, 7, 2, 1, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 0, 0, 4, 8, 1, 1, 7, 9]]
        ]

    for array in arrays:
        print(valid_solution(array))
