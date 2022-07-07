# Python program to convert
# binary tree to doubly linked list
from copy import copy, deepcopy
from typing import Optional, List


class Node(object):
    """Binary tree/ Double Linked List Node class has
    data, left and right child"""

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTreeToDLLConversionApproach1:
    """
     Performs In place conversion from Binary Tree to DLL
     Time Complexity: O(n)
     Space Complexity: O(1)
    """
    def binary_tree_to_dll_util(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root

        if root.left:
            left: Optional[Node] = self.binary_tree_to_dll_util(root.left)

            while left.right:
                left = left.right

            left.right = root
            root.left = left

        if root.right:
            right: Optional[Node] = self.binary_tree_to_dll_util(root.right)

            while right.left:
                right = right.left

            right.left = root
            root.right = right

        return root

    def binary_tree_to_dll(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root

        root = self.binary_tree_to_dll_util(root)

        while root.left:
            root = root.left

        return root


class BinaryTreeToDLLConversionApproach2:
    @staticmethod
    def binary_tree_to_dll(root: Optional[Node]):
        stack: List[Optional[Node]] = []
        current: Optional[Node] = deepcopy(root)
        head: Optional[Node] = None
        tail: Optional[Node] = None

        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()

                if not head:
                    head = current

                if tail:
                    tail.right = current

                tail = current
                current = current.right

        return head


def print_dll(head: Optional[Node]):
    while head is not None:
        print(head.data, end="")
        if head.right:
            print(end=" <-> ")
        head = head.right


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)

    obj1 = BinaryTreeToDLLConversionApproach2()
    head = obj1.binary_tree_to_dll(root)
    print_dll(head)

    print()

    obj = BinaryTreeToDLLConversionApproach1()
    head = obj.binary_tree_to_dll(root)
    print_dll(head)

