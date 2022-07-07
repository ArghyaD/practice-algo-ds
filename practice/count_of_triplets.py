from typing import List, Dict


def get_count_of_triplets(arr: List[int]) -> int:
    """

    :param arr:
    :return:
    """
    count: int = 0
    n: int = len(arr)
    element_map: Dict[int, bool] = {}

    for i in range(n):
        element_map[arr[i]] = True

    for i in range(n):
        for j in range(i+1, n):
            if element_map.get(arr[i] + arr[j]):
                count += 1
                print(arr[i], " ", arr[j], " ", arr[i] + arr[j])

    return count


if __name__ == '__main__':
    arr: List[int] = [1, 5, 3, 2]
    count_of_triplets: int = get_count_of_triplets(arr=arr)
    print(f"Count of triplets for array {arr} is: {count_of_triplets}")
