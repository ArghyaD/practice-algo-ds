from typing import List


def min_heapify(array: List[int], heap_size: int, root_index: int):
    smallest: int = root_index
    left_child: int = 2 * root_index + 1
    right_child: int = 2 * root_index + 2

    if (left_child < heap_size) and (array[left_child] < array[smallest]):
        smallest = left_child

    if (right_child < heap_size) and (array[right_child] < array[smallest]):
        smallest = right_child

    if smallest != root_index:
        array[smallest], array[root_index] = array[root_index], array[smallest]
        min_heapify(array, heap_size, smallest)


def kth_smallest_element(array: List[int], k):
    size = len(array)

    for i in range(size//2, -1, -1):
        min_heapify(array, size, i)

    for i in range(size-1, size - 1 - k, -1):
        array[0], array[i] = array[i], array[0]
        min_heapify(array, i, 0)

    return array[size - k]


if __name__ == "__main__":
    array = [12, 6, 4, 15, 19, 21, 9, 1]
    k = 2
    print(f"{k}th smallest element in {array} is: ", kth_smallest_element(array, k))
