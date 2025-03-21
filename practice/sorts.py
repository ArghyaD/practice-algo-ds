from typing import List


def selection_sort(arr: List[int]):
    n = len(arr)
    for i in range(n-2):
        ith_element: int = arr[i+1]
        pos: int = i + 1
        for j in range(i+2, n):
            if ith_element > arr[j]:
                ith_element = arr[j]
                pos = j
        arr[i], arr[pos] = arr[pos], arr[i]

    print(arr)


if __name__ == "__main__":
    selection_sort([64, 25, 12, 22, 11])
