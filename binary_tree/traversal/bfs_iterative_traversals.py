from typing import Optional, List

from binary_tree.get_maximum_width_and_height import TreeNode


class BfsIterativeTraversals:
    @staticmethod
    def zig_zag_order_using_two_queue(root: Optional[TreeNode]) -> None:
        if not root:
            return None

        queue_1: List[TreeNode] = [root]
        queue_2: List[TreeNode] = []

        while queue_1 or queue_2:
            while queue_1:
                temp: TreeNode = queue_1.pop(0)
                print(temp.val, end=" ")
                if temp.left:
                    queue_2.append(temp.left)
                if temp.right:
                    queue_2.append(temp.right)

            while queue_2:
                temp: TreeNode = queue_2.pop(0)

    @staticmethod
    def zig_zag_order_using_one_doubly_ended_queue(root: Optional[TreeNode]) -> None:
        if not root:
            return None

        stack: List[TreeNode] = [root]
        direction: bool = False  # False denotes right -> left & True denotes left -> right

        while stack:
            count: int = len(stack)

            for i in range(count):
                if not direction:
                    temp: TreeNode = stack.pop()
                else:
                    temp: TreeNode = stack.pop(0)
                print(temp.val, end=" ")
                if temp.left:
                    stack.append(temp.left)
                if temp.right:
                    stack.append(temp.right)
            direction = not direction

    # @staticmethod
    # def spiral_order_using_2d_matrix(root: Optional[BinaryTreeNode]):
    #     """
    #         Clockwise Spiral Traversal of Binary Tree:
    #
    #         Algorithm:
    #             1. First calculate the width of the given tree.
    #             2. Create an auxiliary 2D array of order (width*width)
    #             3. Do level order traversal of the binary tree and store levels in the newly created 2D matrix one by
    #                 one in respective rows. That is, store nodes at level 0 at row indexed 0, nodes at level 1 at row
    #                 indexed 1 and so on.
    #             4. Finally, traverse the 2d array in the below fashion:
    #                 i. Start from the first row from left to right and print elements.
    #                 ii. Then traverse the last row from right to left and print elements.
    #                 iii. Again traverse the second row from left to right and print.
    #                 iv. Then second last row from right to left and so on and repeat the steps until the complete 2-D
    #                  array is traversed.
    #     :param root:
    #     :return:
    #     """
    #
    #     matrix_buffer: List[List[Optional[BinaryTreeNode]]] = [None for]

if __name__ == "__main__":
    root: TreeNode = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.left.right = TreeNode(6)
    root.left.left = TreeNode(7)

    print("Zig Zag Level Order Traversal: ")
    BfsIterativeTraversals.zig_zag_order_using_one_doubly_ended_queue(root)
