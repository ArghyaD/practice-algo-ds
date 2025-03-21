from typing import List


class Solution:
    @staticmethod
    def approach1(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = j = 0
        nums = []

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        if i < m:
            nums.extend(nums1[i:m])

        if j < n:
            nums.extend(nums2[j:n])

        nums1[:] = nums

    @staticmethod
    def approach2(nums1: List[int], m: int, nums2: List[int], n: int):
        i: int = m - 1
        j: int = n - 1
        k: int = m + n - 1
        for i in range(m, k + 1):
            nums1.append(-1)
        print(nums1)
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

if __name__ == '__main__':
    nums1: List[int] = [1, 2, 3]
    nums2: List[int] = [2, 5, 6]
    Solution.approach2(nums1=nums1, m=len(nums1), nums2=nums2, n=len(nums2))

    print(nums1)
