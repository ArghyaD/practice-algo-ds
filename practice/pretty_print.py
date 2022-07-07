class PrettyPrint:
    def solution1(self, A: int) -> None:
        if A < 1:
            return [[None]]
        if A == 1:
            print(1)
            return None

        column_direction = [1, 0, -1, 0]
        row_direction = [0, 1, 0, -1]
        current_direction_index = 0
        digit = A
        n = A * 2 - 1
        lap = n + 2 * (n - 1) + n - 2
        lap_tracker = 0

        current_row = current_column = 0
        seen = [[False for _ in range(n)] for _ in range(n)]
        output_matrix = [[0 for _ in range(n)] for _ in range(n)]

        for _ in range(n * n):
            output_matrix[current_row][current_column] = digit
            seen[current_row][current_column] = True
            next_row = current_row + row_direction[current_direction_index]
            next_column = current_column + column_direction[current_direction_index]

            if (0 <= next_row < n) and (0 <= next_column < n) and not seen[next_row][next_column]:
                current_row = next_row
                current_column = next_column
            else:
                current_direction_index = (current_direction_index + 1) % 4
                current_row += row_direction[current_direction_index]
                current_column += column_direction[current_direction_index]
            lap_tracker += 1
            if lap_tracker >= lap:
                digit -= 1
                lap_tracker = 0
                current_n = digit * 2 - 1
                lap = current_n + 2 * (current_n - 1) + current_n - 2

        i = j = 0
        for _ in range(n * n):
            print(output_matrix[i][j], end=" ")
            j += 1
            if j == n:
                print()
                j = 0
                i += 1

if __name__ == '__main__':
    obj = PrettyPrint()
    obj.solution1(1)

