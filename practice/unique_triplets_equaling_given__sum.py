from typing import List


def unique_triplets_equaling_given_sum(arr: List, sum_value: int):
    unique_triplets: List[List[int]] = []
    size: int = len(arr)
    arr.sort()

    for i in range(size-2):
        if i == 0 or arr[i] > arr[i-1]:
            j: int = i + 1
            k: int = size - 1
            target: int = sum_value - arr[i]
            while j < k:
                if (j > (i + 1)) and arr[j] == arr[j-1]:
                    j += 1
                    continue

                if (k < (size - 1)) and arr[k] == arr[k+1]:
                    k -= 1
                    continue

                left_over_value: int = arr[j] + arr[k]

                if target == left_over_value:
                    unique_triplets.append([arr[i], arr[j], arr[k]])
                    j += 1
                    k -= 1

                if target > left_over_value:
                    j += 1

                if target < left_over_value:
                    k -= 1
    return unique_triplets


if __name__ == "__main__":
    print(unique_triplets_equaling_given_sum([12, 3, 6, 1, 6, 9], 24))
