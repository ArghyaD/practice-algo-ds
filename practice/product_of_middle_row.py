def product_of_middle_row_and_column(matrix):
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    mid_row_index = rows_count // 2
    mid_column_index = columns_count // 2

    mid_row_sum = 1
    mid_column_sum = 1
    for i in range(columns_count):
        mid_row_sum *= matrix[mid_row_index][i]

    for i in range(rows_count):
        mid_column_sum *= matrix[i][mid_column_index]

    print(f"Sum of elements in the middle row is {mid_row_sum}")

    print(f"Sum of elements in the middle column is {mid_column_sum}")


if __name__ == '__main__':
    input_matrix = [
                        [1, 3, 5, 6, 7],
                        [3, 5, 3, 2, 1],
                        [1, 2, 3, 4, 5],
                        [7, 9, 2, 1, 6],
                        [9, 1, 5, 3, 2]
                    ]

    product_of_middle_row_and_column(input_matrix)
