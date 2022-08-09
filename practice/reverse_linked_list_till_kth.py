from copy import deepcopy
from typing import Optional

from practice.reverse_linked_lists import LinkedListNode, print_linked_list


def reverse_linked_list_till_kth(head_ptr: Optional[LinkedListNode], k: int):
    prev: Optional[LinkedListNode] = None
    current: Optional[LinkedListNode] = head_ptr
    count: int = 0
    next_ptr: Optional[LinkedListNode] = None
    while current and count < k:
        next_ptr = current.next
        current.next = prev
        prev = current
        current = next_ptr
        count += 1

    if next_ptr:
        head_ptr.next = reverse_linked_list_till_kth(next_ptr, k)

    return prev


if __name__ == '__main__':
    head = LinkedListNode(5)
    head.next = LinkedListNode(3)
    head.next.next = LinkedListNode(7)
    head.next.next.next = LinkedListNode(2)
    head.next.next.next.next = LinkedListNode(6)
    head.next.next.next.next.next = LinkedListNode(9)
    head.next.next.next.next.next.next = LinkedListNode(8)
    head.next.next.next.next.next.next.next = LinkedListNode(13)
    head.next.next.next.next.next.next.next.next = LinkedListNode(1)
    head.next.next.next.next.next.next.next.next.next = LinkedListNode(7)
    head.next.next.next.next.next.next.next.next.next.next = LinkedListNode(19)

    head = reverse_linked_list_till_kth(head, 3)

    print_linked_list(head)
