from typing import List


def liner_matrix_parser(matrix: List[List[int]]) -> None:
    loop_counter = i = j = 0
    row = len(matrix)
    column = len(matrix[0])
    i = 0
    j = 0

    while True:
        print(matrix[i][j], end=" ")
        j += 1
        if j == column:
            print()
            j = 0
            i += 1
        if i == row:
            break

if __name__ == '__main__':
    matrix: List[List[int]] = [[1, 2, 3, 4, 5, 6, 99, 98, 97],
                               [7, 8, 9, 10, 11, 12, 96, 95, 94],
                               [13, 14, 15, 16, 17, 18, 93, 92, 91],
                               [90, 89, 88, 87, 86, 85, 84, 83, 82],
                               [81, 80, 79, 78, 77, 76, 75, 74, 73],
                               [72, 71, 70, 69, 68, 67, 66, 65, 64]]

    liner_matrix_parser(matrix)
