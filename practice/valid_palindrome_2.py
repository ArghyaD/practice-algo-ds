class Solution:
    def isPalindrome(self, s: str, front: int, rear: int) -> bool:
        while front < rear:
            if s[front] != s[rear]:
                return False
            front += 1
            rear -= 1
        return True


    def validPalindrome(self, s: str) -> bool:
        """
        Given a string s, return true if the s can be palindrome after deleting at most one character from it.
        :param s:
        :return:
        """
        front: int = 0
        rear: int = len(s) - 1
        count = 0
        while front < rear:
            if s[front] != s[rear] and count < 1:
                count += 1
                return self.isPalindrome(s, front + 1, rear) or self.isPalindrome(s, front, rear - 1)
            elif s[front] != s[rear]:
                return False
            else:
                front += 1
                rear -= 1
        return True

if __name__ == "__main__":
    print(Solution().validPalindrome("deeee"))
