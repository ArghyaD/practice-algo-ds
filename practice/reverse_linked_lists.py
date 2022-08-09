from typing import Optional


class LinkedListNode:
    def __init__(self, key: int, next_ptr=None):
        self.key: int = key
        self.next: Optional[LinkedListNode] = next_ptr


def reverse_linked_list(head: Optional[LinkedListNode]):
    prev_ptr: Optional[LinkedListNode] = None
    current_ptr: Optional[LinkedListNode] = head

    next_ptr: Optional[LinkedListNode] = head.next if head else None
    while current_ptr:
        current_ptr.next = prev_ptr
        prev_ptr = current_ptr
        current_ptr = next_ptr
        next_ptr = next_ptr.next if next_ptr else None

    return prev_ptr


def print_linked_list(head: Optional[LinkedListNode]):
    while head:
        print(head.key, end=" ")
        head = head.next


if __name__ == '__main__':
    head = LinkedListNode(5)
    head.next = LinkedListNode(3)
    head.next.next = LinkedListNode(7)
    head.next.next.next = LinkedListNode(2)
    head.next.next.next.next = LinkedListNode(6)

    head = reverse_linked_list(head)

    print_linked_list(head)
