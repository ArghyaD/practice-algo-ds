from typing import List, Optional


def subarray_with_sum_neg(arr: List[int], target_sum: int) -> Optional[List[int]]:
    # This solution will only work for positive & negative numbers in the list
    current_sum: int = 0
    sum_map = {}

    for i in range(len(arr)):
        current_sum += arr[i]
        sum_to_check = current_sum - target_sum

        if sum_to_check == 0:
            return arr[0: i + 1]

        if sum_map.get(sum_to_check) is not None:
            return arr[(sum_map[sum_to_check] + 1): i + 1]

        sum_map[current_sum] = i

    return None


def subarray_with_sum(arr: List[int], target_sum: int) -> Optional[List[int]]:
    # This solution will only work for positive numbers in the list

    n: int = len(arr)
    temp_sum: int = arr[0]
    j = 0
    for i in range(1, n):
        while (temp_sum > target_sum) and j < i - 1:
            temp_sum -= arr[j]
            j += 1

        if temp_sum == target_sum:
            return arr[j: i]

        temp_sum += arr[i]
    return None


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 15
    print(f"For array: {array} and target sum: {target}")
    print(f"Solution for only positive elements: {subarray_with_sum(arr=array, target_sum=target)}")

    array = [2, -1, -2, 3, -10, 20]
    target = 10
    print(f"For array: {array} and target sum: {target}")
    print(f"Solution for negative elements handled: {subarray_with_sum_neg(arr=array, target_sum=target)}")
