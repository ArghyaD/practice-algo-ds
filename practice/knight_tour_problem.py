from typing import List


class KnightTourProblem:
    def __init__(self, size: int):
        self.size: int = size
        self.board: List[List[int]] = [[-1 for _ in range(self.size)] for _ in range(self.size)]
        self.cells_covered: int = 1
        self.board[0][0] = 0   # Assuming the starting point is top-left corner
        self.move_x: List[int] = [2, 1, -1, -2, -2, -1,  1,  2]
        self.move_y: List[int] = [1, 2,  2,  1, -1, -2, -2, -1]

    def print_solution(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.board[i][j], end="\t")
            print()

    def find_solution_using_backtracking(self, current_x, current_y):
        if self.cells_covered == self.size * self.size:
            print("Coming out at L 21")
            return True

        # A knight can move in 8 different ways
        for i in range(8):
            next_x = current_x + self.move_x[i]
            next_y = current_y + self.move_y[i]

            if self._is_move_valid(next_x, next_y):
                self.board[next_x][next_y] = self.cells_covered
                self.cells_covered += 1

                if self.find_solution_using_backtracking(next_x, next_y):
                    return True
                self.board[next_x][next_y] = -1
                self.cells_covered -= 1

        return False

    def _is_move_valid(self, next_x: int, next_y: int):
        if 0 <= next_x < self.size and 0 <= next_y < self.size and self.board[next_x][next_y] == -1:
            return True
        return False


if __name__ == '__main__':
    size = 8
    obj = KnightTourProblem(size)

    if obj.find_solution_using_backtracking(0, 0):
        obj.print_solution()
    else:
        print("Solution doesn't exist")
