
# def lucky_number_in_matrix(matrix):
#     '''
#         A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
#     :param matrix:
#     :return:
#     '''
#     row_count = len(matrix)
#     column_count = len(matrix[0])
#     for i in range(row_count):
#         min_element_in_row = matrix[i][0]
#         for j in range(column_count):
#             if
from typing import List



def luckyNumbers (matrix: List[List[int]]) -> List[int]:
    return list({min(row) for row in matrix} & \
                {max(col) for col in zip(*matrix)});

if __name__ == '__main__':
    input_matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    print(*input_matrix)
    print(input_matrix)
    # for col in zip(*input_matrix):
    #     print(col)
    # print(luckyNumbers(input_matrix))