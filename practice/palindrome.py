class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
            An integer is a palindrome when it reads the same backward as forward.
            Complexity: O(n) where n = len(int(x))
        :param x: The number to check palindrome for
        :return: true if it is a palindrome number, false otherwise.
        """
        x_str: str = str(x)
        front: int = 0
        rear: int = len(x_str) - 1

        while front <= rear:
            if x_str[front] != x_str[rear]:
                return False
            front += 1
            rear -= 1

        return True

    def isPalindromeBetter(self, x: int) -> bool:
        """
            An integer is a palindrome when it reads the same backward as forward.
            Complexity: O(log10 x) where
        :param x: The number to check palindrome for
        :return: true if it is a palindrome number, false otherwise.
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_x: int = 0
        while x > reversed_x:
            reversed_x = (reversed_x * 10) + x % 10
            x = int(x / 10)

        if x == reversed_x or x == int(reversed_x/10):
            return True
        return False


if __name__ == "__main__":
    print(Solution().isPalindrome(555))
    print(Solution().isPalindrome(121))
    print(Solution().isPalindrome(-121))

    print(Solution().isPalindromeBetter(555))
    print(Solution().isPalindromeBetter(121))
    print(Solution().isPalindromeBetter(-121))
