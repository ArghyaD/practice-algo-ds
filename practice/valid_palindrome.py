from typing import List


class Solution:
    def _get_lower_alphanumerics(self, s: str) -> List[str]:
        buffer: List[str] = []
        for i in s:
            ascii_value = ord(i)
            if 48 <= ascii_value <= 57 or 65 <= ascii_value <= 90 or 97 <= ascii_value <= 122:
                buffer.append(i.lower())
        return buffer

    def checkPalindromeByMidReverseAlgorithm(self, s: str) -> bool:
        """
            A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
             non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include
              letters and numbers.
        :param s:
        :return:
        """
        n = len(s)
        if 0 <= n <=1:
            return True

        buffer: List[str] = self._get_lower_alphanumerics(s)

        mid_reversed_buffer: List[str] = []
        while len(buffer) > len(mid_reversed_buffer):
            mid_reversed_buffer.append(buffer.pop())

        if buffer == mid_reversed_buffer or buffer == mid_reversed_buffer[0:-1]:
            return True
        return False

    def checkPalindromeByTwoPointerAlgorithm(self, s: str) -> bool:
        """
            A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
             non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include
              letters and numbers.
        :param s:
        :return:
        """
        n = len(s)
        if 0 <= n <= 1:
            return True

        buffer: List[str] = self._get_lower_alphanumerics(s)

        front: int = 0
        rear: int = len(buffer) - 1

        while front < rear:
            if buffer[front] != buffer[rear]:
                return False
            front += 1
            rear -= 1
        return True

