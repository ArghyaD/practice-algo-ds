from typing import List


class SubArrayCountWithOddProduct:
    def solution(self, arr: List[int]) -> int:
        """
            Odd products can only be there when all elements whose product we see are all odd numbers themselves.
            So, the idea is to count the number of consecutive odd numbers in the array and then calculate the number
            of sub-arrays. The number of sub-arrays can be calculated using the formula n*(n+1)/2 where n is the number
            of elements in the sub-array.

        :param arr:
        :return:
        """
        count: int = 0
        result: int = 0
        for val in arr:
            if (val % 2) == 1:
                count += 1
            else:
                result += (count*(count+1)) // 2
                count = 0

        # This is for the last sub-array of all odd elements (if any) which doesn't have a trailing even element.
        result += (count * (count + 1)) // 2
        return result


def get_length(resource_name: List):
    return len(resource_name)


if __name__ == '__main__':
    obj = SubArrayCountWithOddProduct()
    result = obj.solution(arr=[5, 1, 2, 3, 4, 7, 2, 1, 9])
    print(result)