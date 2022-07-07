from typing import Optional, List

from binary_tree.get_maximum_width_and_height import TreeNode


class DfsIterativeTraversalsUsingStack:

    @staticmethod
    def top(stack: List[TreeNode]) -> Optional[TreeNode]:
        if stack:
            return stack[-1]
        return None

    @staticmethod
    def inorder_traversal(root: Optional[TreeNode]):
        current: Optional[TreeNode] = root
        stack: List[TreeNode] = []

        while current or stack:
            if current:
                stack.append(current)

                current = current.left
            else:
                current = stack.pop()

                print(current.val, end=" ")

                current = current.right

    @staticmethod
    def preorder_traversal(root: Optional[TreeNode]):
        current: Optional[TreeNode] = root
        stack: List[TreeNode] = []

        while current or stack:
            if current:
                stack.append(current)

                print(current.val, end=" ")

                current = current.left
            else:
                current = stack.pop()

                current = current.right

    @staticmethod
    def postorder_traversal_using_two_stacks(root: Optional[TreeNode]):
        """
            Algorithm:
                1. Push root to first stack.
                2. Loop while first stack is not empty
                   2.1 Pop a node from first stack and push it to second stack
                   2.2 Push left and right children of the popped node to first stack
                3. Print contents of second stack

        :param root:
        :return:
        """
        stack_one: List[TreeNode] = []
        stack_two: List[TreeNode] = []

        stack_one.append(root)

        while stack_one:
            binary_tree_node: TreeNode = stack_one.pop()

            stack_two.append(binary_tree_node)

            if binary_tree_node.left:
                stack_one.append(binary_tree_node.left)

            if binary_tree_node.right:
                stack_one.append(binary_tree_node.right)

        while stack_two:
            binary_tree_node: TreeNode = stack_two.pop()

            print(binary_tree_node.val, end=" ")

    @staticmethod
    def postorder_traversal_using_one_stack(root: Optional[TreeNode]):
        """
            Algorithm:
                1.1 Create an empty stack
                2.1 Do following while root is not NULL
                    a) Push root's right child and then root to stack.
                    b) Set root as root's left child.
                2.2 Pop an item from stack and set it as root.
                    a) If the popped item has a right child and the right child
                       is at top of stack, then remove the right child from stack,
                       push the root back and set root as root's right child.
                    b) Else print root's data and set root as NULL.
                2.3 Repeat steps 2.1 and 2.2 while stack is not empty Or the root is Null.

        :param root:
        :return:
        """
        stack: List[TreeNode] = []

        while root or stack:
            if root:
                if root.right:
                    stack.append(root.right)

                stack.append(root)
                root = root.left

            else:
                root = stack.pop()

                if root.right and root.right == DfsIterativeTraversalsUsingStack.top(stack):
                    stack.pop()
                    stack.append(root)
                    root = root.right

                else:
                    print(root.val, end=" ")

                    root = None


if __name__ == "__main__":

    # Forming a BST
    bst_root = TreeNode(10)
    bst_root.left = TreeNode(7)
    bst_root.right = TreeNode(15)
    bst_root.left.left = TreeNode(5)
    bst_root.left.right = TreeNode(9)
    bst_root.right.right = TreeNode(19)

    print("\nInorder Traversal: ", end="")
    DfsIterativeTraversalsUsingStack.inorder_traversal(bst_root)

    print("\nPreorder Traversal: ", end="")
    DfsIterativeTraversalsUsingStack.preorder_traversal(bst_root)

    print("\nPostorder Traversal with Two stacks: ", end="")
    DfsIterativeTraversalsUsingStack.postorder_traversal_using_two_stacks(bst_root)

    print("\nPostorder Traversal with One stack: ", end="")
    DfsIterativeTraversalsUsingStack.postorder_traversal_using_one_stack(bst_root)
