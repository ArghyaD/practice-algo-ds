from typing import List


def missing_number_in_array_using_xor(array: List[int]) -> int:
    # NOT SURE IF IT WORKS
    # SAW THE SOLUTION IN THE DISCUSSION
    xr: int = 0
    for i in array:
        xr ^= i
        print(i, xr)
    for i in range(1, (len(array) + 1)):
        xr ^= i
        print(i, xr)
    return xr


def missing_number_in_array(array: List[int]) -> int:
    n: int = len(array)
    perfect_sum: int = int(((n + 1) * (n + 2)) / 2)
    for i in array:
        perfect_sum -= i
    return perfect_sum


if __name__ == '__main__':
    input_list: List[int] = [1, 7, 4, 3, 6, 5]
    print(missing_number_in_array(input_list))
