from typing import List


def kth_smallest_element(elements: List[int], low: int, high: int, k):
    if 0 < k <= (high - low + 1):
        pk = lomutoro_partition(elements, low, high)

        if pk - low == (k - 1):
            return elements[pk]

        if pk - low > (k - 1):
            return kth_smallest_element(elements, low, pk - 1, k)
        return kth_smallest_element(elements, pk + 1, high, k - 1 - (pk - low))


def quick_sort(elements: List[int], low: int, high: int):
    if low < high:
        pk = lomutoro_partition(elements, low, high)

        # pk = hoare_partition(elements, low, high)

        # while using lomutoro's partition algorithm, call the quick sort excluding
        # the partition position
        quick_sort(elements, low, pk - 1)

        # while using hoare's partition algorithm, call the quick sort including
        # the partition position
        # quick_sort(elements, low, pk)
        quick_sort(elements, pk + 1, high)


def lomutoro_partition(elements: List[int], low: int, high: int):
    pivot: int = elements[high]
    i = low

    for j in range(low, high):
        if elements[j] >= pivot:
            elements[i], elements[j] = elements[j], elements[i]
            i += 1
    elements[i], elements[high] = elements[high], elements[i]
    return i


def hoare_partition(elements: List[int], low: int, high: int):
    i: int = low - 1
    j: int = high + 1
    pivot: int = elements[low]

    while True:
        i += 1
        while elements[i] < pivot:
            i += 1

        j -= 1
        while elements[j] > pivot:
            j -= 1

        if i >= j:
            return j

        elements[i], elements[j] = elements[j], elements[i]


if __name__ == '__main__':
    input_list: List[int] = [5, 2, 3, 9, 17, 6, 9, 1]
    #
    # print(f"List before sorting {input_list}")
    #
    # quick_sort(input_list, 0, len(input_list) - 1)
    #
    # print(f"List after sorting {input_list}")
    print(kth_smallest_element(input_list, 0, len(input_list) - 1, 3))