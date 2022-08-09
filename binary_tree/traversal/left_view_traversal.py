from typing import Optional, List

from binary_tree.get_maximum_width_and_height import TreeNode


def right_view_traversal(root: Optional[TreeNode]):
    queue: List[TreeNode] = [root]

    while queue:
        size = len(queue)

        for i in range(size):
            temp = queue.pop(0)

            if i == 0:
                print(temp.val, end=" ")
            if temp.right:
                queue.append(temp.right)
            if temp.left:
                queue.append(temp.left)


def left_view_traversal(root: Optional[TreeNode]):
    queue: List[TreeNode] = [root]

    while queue:
        size = len(queue)

        for i in range(size):
            temp = queue.pop(0)

            if i == 0:
                print(temp.val, end=" ")
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)


def left_view_recursive_traversal_util(root: Optional[TreeNode], level: int, max_level) -> None:
    if not root:
        return None
    print(f"[DEBUG] Node: {root.val}, level: {level}, max_level:{max_level[0]}")
    if max_level[0] < level:
        print(root.val)
        max_level[0] = level
    left_view_recursive_traversal_util(root.left, level + 1, max_level)
    left_view_recursive_traversal_util(root.right, level + 1, max_level)


def left_view_recursive_traversal(root: Optional[TreeNode]) -> None:
    left_view_recursive_traversal_util(root, 1, [0])


if __name__ == '__main__':
    root: TreeNode = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # left_view_iterative_traversal(root)
    left_view_recursive_traversal(root)

