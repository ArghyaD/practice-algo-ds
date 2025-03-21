from typing import List


def merge(arr: List[int], low, mid, high):
    i = j = 0
    k = low
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1

def space_optimized_merge(arr, low, mid, high):
    i = low
    j = mid + 1
    print(f"Initial: {arr[low:high + 1]}")
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            i += 1
        else:
            temp = arr[j]
            k = j
            while k > i:
                arr[k] = arr[k - 1]
                k -= 1
            arr[i] = temp
            i += 1
            mid += 1
            j += 1


def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)

        space_optimized_merge(arr, low, mid, high)


if __name__ == '__main__':
    arr = [45, 12, 14, 34, 56, 67, 87, 16, 19, 78]
    print(f"Before sort {arr}")
    merge_sort(arr, 0, len(arr) - 1)
    print(f"After sort {arr}")
