from typing import List


class MaximumSumSubarray:
    def kadane_algorithm(self, arr: List[int]) -> int:
        max_current: int = arr[0]
        max_global: int = arr[0]
        for i in range(1, len(arr)):
            max_current = max(arr[i], max_current + arr[i])
            if max_current > max_global:
                max_global = max_current
        return max_global


if __name__ == '__main__':
    obj = MaximumSumSubarray()
    array: List[int] = [1, 2, 3, -2, 5]
    print(f"Maximum sub-array sum of array {array} is {obj.kadane_algorithm(array)}")