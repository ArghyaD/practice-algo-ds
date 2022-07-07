from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_linked_list(self, head: Optional[ListNode]):
        prev: Optional[ListNode] = None
        curr: Optional[ListNode] = head

        while curr:
            next_element: Optional[ListNode] = curr.next
            curr.next = prev
            prev = curr
            curr = next_element

        return prev

    def get_mid(self, head: Optional[ListNode]):
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow.next

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        mid_reversed_list: Optional[ListNode] = self.reverse_linked_list(self.get_mid(head))

        while mid_reversed_list:
            if mid_reversed_list.val != head.val:
                return False
            mid_reversed_list = mid_reversed_list.next
            head = head.next
        return True

    def isPalindromeDeprecated(self, head: Optional[ListNode]) -> bool:
        # ISSUE: This approach takes the palindrome values and converts it into an integer
        # as well as it's reverse integer. If either of them exceeds the limit of MAX_INT.
        # it fails.

        num: int = 0
        multiplier: int = 1
        rev_num: int = 0
        while head:
            num = num * 10 + head.val
            rev_num = rev_num + head.val * multiplier
            multiplier *= 10
            head = head.next

        if num == rev_num:
            return True
        return False
