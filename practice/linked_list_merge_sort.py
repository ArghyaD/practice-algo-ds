from typing import Optional


class Node:
    def __init__(self, data, next_ptr=None):
        self.data: int = data
        self.next: Node = next_ptr


def get_middle(head: Optional[Node]):
    slow: Node = head
    fast: Node = head

    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_sorted_linked_lists(head_1: Optional[Node], head_2: Optional[Node]):
    result: Optional[Node] = None
    current: Optional[Node] = None

    while head_1 and head_2:
        if head_1.data < head_2.data:
            if not result:
                result = Node(head_1.data)
                current = result
            else:
                current.next = Node(head_1.data)
                current = current.next
            head_1 = head_1.next
        else:
            if not result:
                result = Node(head_2.data)
                current = result
            else:
                current.next = Node(head_2.data)
                current = current.next
            head_2 = head_2.next
    if head_1:
        current.next = head_1
    else:
        current.next = head_2
    return result


def linked_list_merged_sort(head: Node):
    if not head or not head.next:
        return head
    mid = get_middle(head)
    mid_next = mid.next

    mid.next = None

    left: Optional[Node] = linked_list_merged_sort(head)
    right: Optional[Node] = linked_list_merged_sort(mid_next)

    output_list = merge_sorted_linked_lists(left, right)

    return output_list


def print_list(head: Optional[Node]):
    current: Optional[Node] = head

    while current:
        print(current.data, end="")
        if current.next:
            print(" -> ", end="")
        current = current.next


if __name__ == '__main__':
    head = Node(7)
    head.next = Node(3)
    head.next.next = Node(2)
    head.next.next.next = Node(19)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(9)
    head.next.next.next.next.next.next = Node(11)
    head.next.next.next.next.next.next.next = Node(21)
    head.next.next.next.next.next.next.next.next = Node(1)

    print("Unsorted Linked List")
    print_list(head)

    sorted_list = linked_list_merged_sort(head)

    print("\nSorted Linked List")
    print_list(sorted_list)
