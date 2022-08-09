from typing import Optional, List

from binary_tree.get_maximum_width_and_height import TreeNode


class DfsIterativeTraversalsUsingMorrisAlgorithm:
    @staticmethod
    def inorder_traversal(root: Optional[TreeNode]):
        """
        1. Initialize current as root
        2. While current is not NULL
           If the current does not have left child
              a) Print current’s data
              b) Go to the right, i.e., current = current->right
           Else
              a) Find rightmost node in current left subtree OR
                      node whose right child == current.
                 If we found right child == current
                     a) Update the right child as NULL of that node whose right child is current
                     b) Print current’s data
                     c) Go to the right, i.e. current = current->right
                 Else
                     a) Make current as the right child of that rightmost
                        node we found; and
                     b) Go to this left child, i.e., current = current->left
        :param root:
        :return:
        """

        current: Optional[TreeNode] = root

        while current:
            if not current.left:
                print(current.val, end=" ")
                current = current.right

            else:
                right_most_node_in_left_subtree: Optional[TreeNode] = current.left

                while right_most_node_in_left_subtree.right and right_most_node_in_left_subtree.right is not current:
                    right_most_node_in_left_subtree = right_most_node_in_left_subtree.right

                if not right_most_node_in_left_subtree.right:
                    # It means the left subtree is not visited yet. Hence, we need to visit it and to come back to the
                    # root node, we need the right most node in the left subtree's right child to point to the current
                    # node.
                    right_most_node_in_left_subtree.right = current
                    current = current.left
                else:
                    # It means the left subtree has already been visited and a link to the current node from the right
                    # most node of left subtree's right child already exists. Hence, we can print the node now and visit
                    # the right subtree.
                    right_most_node_in_left_subtree.right = None
                    print(current.val, end=" ")
                    current = current.right

    @staticmethod
    def preorder_traversal(root: Optional[TreeNode]):
        """
            1. Initialize current as root
            2. While current is not NULL
               If the current does not have left child
                  a) Print current’s data
                  b) Go to the right, i.e., current = current->right
               Else
                  a) Find rightmost node in current left subtree OR
                          node whose right child == current.
                     If we found right child == current
                         a) Update the right child as NULL of that node whose right child is current
                         b) Go to the right, i.e. current = current->right
                     Else
                         a) Make current as the right child of that rightmost
                            node we found; and
                         b) Print current’s data
                         c) Go to this left child, i.e., current = current->left
            :param root:
            :return:
        """
        current: Optional[TreeNode] = root
        while current:
            if not current.left:
                print(current.val, end=" ")
                current = current.right
            else:
                right_most_node_in_left_subtree = current.left

                while right_most_node_in_left_subtree.right and right_most_node_in_left_subtree.right is not current:
                    right_most_node_in_left_subtree = right_most_node_in_left_subtree.right

                if not right_most_node_in_left_subtree.right:
                    print(current.val, end=" ")
                    right_most_node_in_left_subtree.right = current
                    current = current.left
                else:
                    right_most_node_in_left_subtree.right = None
                    current = current.right

    @staticmethod
    def postorder_traversal(root: Optional[TreeNode]):
        result: List[int] = []

        current: Optional[TreeNode] = root

        while current:

            if not current.right:
                result.append(current.val)
                current = current.left
            else:
                left_most_node_in_right_subtree: TreeNode = current.right

                while left_most_node_in_right_subtree.left and left_most_node_in_right_subtree.left is not current:
                    left_most_node_in_right_subtree = left_most_node_in_right_subtree.left

                if not left_most_node_in_right_subtree.left:
                    result.append(current.val)
                    left_most_node_in_right_subtree.left = current
                    current = current.right

                else:
                    left_most_node_in_right_subtree.left = None
                    current = current.left

        while result:
            print(result.pop(), end=" ")


if __name__ == "__main__":

    # Forming a BST
    bst_root = TreeNode(10)
    bst_root.left = TreeNode(7)
    bst_root.right = TreeNode(15)
    bst_root.left.left = TreeNode(5)
    bst_root.left.right = TreeNode(9)
    bst_root.right.right = TreeNode(19)

    print("\nInorder Traversal: ", end="")
    DfsIterativeTraversalsUsingMorrisAlgorithm.inorder_traversal(bst_root)

    print("\nPreorder Traversal: ", end="")
    DfsIterativeTraversalsUsingMorrisAlgorithm.preorder_traversal(bst_root)

    print("\nPost Order Traversal: ", end="")
    DfsIterativeTraversalsUsingMorrisAlgorithm.postorder_traversal(bst_root)
