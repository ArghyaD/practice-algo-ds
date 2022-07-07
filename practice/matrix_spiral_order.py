from time import time
from timeit import default_timer
from typing import List


class MatrixSpiralOrder:
    @staticmethod
    def matrix_spiral_order_simple_approach(m: int, n: int, a: List[List[int]]) -> None:
        """
            Time Complexity: O(m*n) ~= O(n^2)
            Space Complexity: O(1)
        :param m: row count of matrix
        :param n: column count of matrix
        :param a: matrix
        :return:
        """
        k: int = 0  # starting index of row
        l: int = 0  # starting index of column

        while k < m and l < n:
            for i in range(l, n):
                print(a[k][i], end=" ")

            k += 1

            for i in range(k, m):
                print(a[i][n - 1], end=" ")

            n -= 1

            if k < m:
                for i in range(n - 1, l - 1, -1):
                    print(a[m - 1][i], end=" ")

                m -= 1

            if l < n:
                for i in range(m - 1, k - 1, -1):
                    print(a[i][l], end=" ")

                l += 1

    @staticmethod
    def matrix_spiral_order_simulation_approach(row: int, column: int, matrix: List[List[int]]):
        seen: List[List[int]] = [[False for _ in range(column)] for _ in range(row)]

        current_row: int = 0
        current_column: int = 0
        column_direction: List[int] = [1, 0, -1, 0]
        row_direction: List[int] = [0, 1, 0, -1]

        current_direction: int = 0

        for _ in range(row * column):
            print(matrix[current_row][current_column], end=" ")
            seen[current_row][current_column] = True
            next_row: int = current_row + row_direction[current_direction]
            next_column: int = current_column + column_direction[current_direction]

            if (0 <= next_row < row) and (0 <= next_column < column) and not seen[next_row][next_column]:
                current_row = next_row
                current_column = next_column
            else:
                current_direction = (current_direction + 1) % 4
                current_row += row_direction[current_direction]
                current_column += column_direction[current_direction]


if __name__ == "__main__":
    matrix: List[List[int]] = [[1, 2, 3, 4, 5, 6, 99, 98, 97],
                               [7, 8, 9, 10, 11, 12, 96, 95, 94],
                               [13, 14, 15, 16, 17, 18, 93, 92, 91],
                               [90, 89, 88, 87, 86, 85, 84, 83, 82],
                               [81, 80, 79, 78, 77, 76, 75, 74, 73],
                               [72, 71, 70, 69, 68, 67, 66, 65, 64]]

    R: int = len(matrix)
    C: int = len(matrix[0])

    obj = MatrixSpiralOrder()
    print("Using Simple Approach:")
    start_time = default_timer()
    obj.matrix_spiral_order_simple_approach(R, C, matrix)
    end_time = default_timer()
    print("\nTime Complexity: O(row * column). \nSpace Complexity: O(1)")
    print(f"Time elapsed: {end_time - start_time}")

    print("\nUsing Simulation Approach:")
    start_time = default_timer()
    obj.matrix_spiral_order_simulation_approach(R, C, matrix)
    end_time = default_timer()
    print("\nTime Complexity: O(n). \nSpace Complexity: O(row * column)")
    print(f"Time elapsed: {end_time - start_time}")
