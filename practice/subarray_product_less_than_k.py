from typing import List


class SubArrayProductLessThanK:
    def solution(self, nums: List[int], k: int) -> int:
        """
            Considerations:
                1 <= nums.length <= 3 * 104
                1 <= nums[i] <= 1000
                0 <= k <= 106
        """
        if k < 1:
            return 0
        n = len(nums)
        left = 0
        prod = 1
        result =0

        for right, num in enumerate(nums):
            prod *= num

            while prod >= k:
                prod //= nums[left]
                left += 1

            result += right - left + 1

            print(f"left: {left}")
            print(f"right: {right}")
            print(f"prod: {prod}")
            print(f"result: {result}")
        return result

if __name__ == '__main__':
    obj = SubArrayProductLessThanK()
    print(obj.solution([10,5,2,6], k=100))
