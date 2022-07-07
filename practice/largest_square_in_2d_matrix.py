from typing import List


class LargestSquareIn2dMatrix:
    @staticmethod
    def solution_1(matrix: List[List[int]]) -> None:
        row: int = len(matrix)
        column: int = len(matrix[0])

        auxilliary_mem: List[List[int]] = [[0 for _ in range(column)] for _ in range(row)]

        max_size: int = 0

        for i in range(row):
            auxilliary_mem[i][0] = matrix[i][0]

        for i in range(1, column):
            auxilliary_mem[0][i] = matrix[0][i]

        for i in range(1, row):
            for j in range(1, column):
                if matrix[i][j]:
                    auxilliary_mem[i][j] = min(auxilliary_mem[i-1][j-1], auxilliary_mem[i-1][j], auxilliary_mem[i][j-1]) + 1
                    max_size = max(max_size, auxilliary_mem[i][j])
        for i in range(max_size):
            for j in range(max_size):
                print(1, end="\t")
            print()

    @staticmethod
    def solution_2(matrix: List[List[int]]):
        """
            Space Efficient Solution
        :param matrix:
        :return:
        """
        row: int = len(matrix)
        column: int = len(matrix[0])

        max_size: int = 0

        auxilliary_mem: List[List[int]] = [[0 for i in range(column)]for j in range(2)]

        for i in range(row):
            for j in range(column):
                element = matrix[i][j]
                if j and element:
                    element = 1 + min(auxilliary_mem[1][j-1], auxilliary_mem[0][j-1], auxilliary_mem[1][j])
                    max_size = max(max_size, element)

                auxilliary_mem[0][j] = auxilliary_mem[1][j]
                auxilliary_mem[1][j] = element

        for i in range(max_size):
            for j in range(max_size):
                print(1, end="\t")
            print()


if __name__ == "__main__":
    m: List[List[int]] = \
        [
            [0, 1, 1, 0, 1],
            [1, 1, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0]
        ]
    LargestSquareIn2dMatrix.solution_1(m)
    print()
    LargestSquareIn2dMatrix.solution_2(m)
