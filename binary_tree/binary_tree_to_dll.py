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
     Space Complexity: O(n)
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

        current = deepcopy(root)
        current = self.binary_tree_to_dll_util(current)

        while current.left:
            current = current.left

        return current


class BinaryTreeToDLLConversionApproach2:
    @staticmethod
    def binary_tree_to_dll(root: Optional[Node]):
        stack: List[Optional[Node]] = []
        current: Optional[Node] = deepcopy(root)  # deep copy is not required here
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


class BinaryTreeToDLLConversionApproach3:
    """
     Performs In place conversion from Binary Tree to DLL
     Time Complexity: O(n)
     Space Complexity: O(1)
    """
    @staticmethod
    def binary_tree_to_dll(root: Optional[Node]):
        current: Optional[Node] = deepcopy(root)
        head: Optional[Node] = None
        tail: Optional[Node] = None

        while current:
            if not current.left:
                if not head:
                    head = current
                else:
                    tail.right = current
                tail = current
                current = current.right
            else:
                inorder_predecessor: Node = current.left
                while inorder_predecessor.right and inorder_predecessor.right is not current:
                    inorder_predecessor = inorder_predecessor.right

                if not inorder_predecessor.right:
                    inorder_predecessor.right = current
                    current = current.left
                else:
                    tail.right = current
                    tail = current
                    current = current.right
        print(head.data)
        return head


def print_dll(head: Optional[Node]):
    current = head
    print("\nPrinting from head: ")
    while current:
        left = current.left.data if current.left else None
        right = current.right.data if current.right else None
        print(f"({left}) {current.data} ({right})", end="")

        if current.right:
            print(end=" <=> ")
        current = current.right


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

    print("\n*********************************************************************************")

    obj = BinaryTreeToDLLConversionApproach1()
    head = obj.binary_tree_to_dll(root)
    print_dll(head)

    print("\n*********************************************************************************")

    obj = BinaryTreeToDLLConversionApproach3()
    head = obj.binary_tree_to_dll(root)
    print_dll(head)

    print("\n*********************************************************************************")
