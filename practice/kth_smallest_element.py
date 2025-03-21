from typing import List


def min_heapify(array: List[int], heap_size: int, root_index: int):
    current = root_index

    while True:
        largest = current
        left = 2 * largest + 1
        right = 2 * largest + 2

        if (left < heap_size) and array[left] < array[largest]:
            largest = left

        if (right < heap_size) and array[right] < array[largest]:
            largest = right

        if current == largest:
            break

        array[current], array[largest] = array[largest], array[current]
        current = largest


def kth_smallest_element(array: List[int], k):
    size = len(array)

    for i in range(size//2, -1, -1):
        min_heapify(array, size, i)

    for i in range(size-1, size - 1 - k, -1):
        array[0], array[i] = array[i], array[0]
        min_heapify(array, i, 0)

    return array[size - k]


def heap_sort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        min_heapify(arr, heap_size=n, root_index=i)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[0], arr[i]
        min_heapify(arr, heap_size=i, root_index=0)


if __name__ == "__main__":
    array = [12, 6, 4, 15, 19, 21, 9, 1]
    heap_sort(arr=array)
    print(array)
    # k = 2
    # print(f"{k}th smallest element in {array} is: ", kth_smallest_element(array, k))
