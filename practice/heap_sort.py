from typing import List


class HeapSort:
    def _heapify(self, array: List[int], heap_size: int, root_index: int):
        largest: int = root_index
        left_child: int = 2 * root_index + 1
        right_child: int = 2 * root_index + 2

        if (left_child < heap_size) and (array[largest] < array[left_child]):
            largest = left_child

        if (right_child < heap_size) and (array[largest] < array[right_child]):
            largest = right_child

        if largest != root_index:
            array[largest], array[root_index] = array[root_index], array[largest]

            self._heapify(array, heap_size, largest)

    def heap_sort(self, array: List[int]):
        n: int = len(array)

        # Build Max
        for i in range(n//2 - 1, -1, -1):
            self._heapify(array, n, i)

        # At this point we have a max heap. Hence, the largest element is at the root.
        # So, at each step, extract the root to the last position and call heapify by
        # reducing the size of heap by 1
        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self._heapify(array, i, 0)


if __name__ == "__main__":
    obj = HeapSort()
    array: List[int] = [14, 5, 3, 6, 12, 1, 19]
    print("Unsorted Array: ", array)
    obj.heap_sort(array)

    print("Sorted Array: ", array)
