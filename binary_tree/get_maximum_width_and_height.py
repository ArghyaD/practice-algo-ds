import sys
from collections import defaultdict, deque
from typing import Optional, List, Deque, Tuple




class TreeNode:
    def __init__(self, data):
        self.val: int = data
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


def recursive_max_height(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(recursive_max_height(root.left), recursive_max_height(root.right))


def iterative_max_height(root: Optional[TreeNode]) -> int:
    max_height: int = 0
    queue: Deque = deque([root])
    while queue:
        elements_in_level = len(queue)
        for i in range(elements_in_level):
            temp = queue.popleft()
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        max_height += 1
    return max_height


def iterative_max_width(root: Optional[TreeNode]) -> int:
    queue: List[Optional[TreeNode]] = [root]
    max_width: int = 0
    while queue:
        current_level_width = len(queue)
        max_width = current_level_width if max_width < current_level_width else max_width
        for i in range(current_level_width):
            temp: TreeNode = queue.pop(0)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
    return max_width


def get_maximum_width_including_non_terminal_null_nodes(root: Optional[TreeNode]) -> int:
    """
        This one includes null nodes between the leftmost & rightmost null node
    :param root:
    :return:
    """
    max_width: int = 0
    degree_map = defaultdict(list)
    queue: Deque[Tuple] = deque([(root, 0, 1)])

    while queue:
        node, degree, index = queue.popleft()
        degree_map[degree].append(index)
        if node.left:
            queue.append((node.left, (degree + 1), index * 2))
        if node.right:
            queue.append((node.right, (degree + 1), (index * 2 + 1)))

    for each in degree_map.values():
        max_width = max(max_width, each[-1] - each[0] + 1)
    return max_width

#Practice
def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return None
    container_queue: Deque[Optional[TreeNode]] = deque([root])
    flag = False
    out_list: List[List[int]] = []

    while container_queue:
        level_width = len(container_queue)
        level_queue: List[int] = []

        for i in range(level_width):

            if flag:
                temp: TreeNode = container_queue.pop()
                if temp.left:
                    container_queue.appendleft(temp.left)
                if temp.right:
                    container_queue.appendleft(temp.right)
            else:
                temp: TreeNode = container_queue.popleft()
                if temp.right:
                    container_queue.append(temp.right)
                if temp.left:
                    container_queue.append(temp.left)
            level_queue.append(temp.val)

        flag = not flag
        out_list.append(level_queue)
    return out_list


class Solution:
    def max_ancestor_diff_util(self, root: Optional[TreeNode], current_max: int, current_min: int) -> int:
        if not root:
            return 0
        self.answer = max(self.answer, abs(root.val - current_max), abs(root.val - current_min))
        current_max = max(current_max, root.val)
        current_min = min(current_min, root.val)

        self.max_ancestor_diff_util(root.left, current_max, current_min)
        self.max_ancestor_diff_util(root.right, current_max, current_min)

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.answer: int = 0
        self.max_ancestor_diff_util(root=root, current_max=root.val, current_min=root.val)
        return self.answer


if __name__ == "__main__":
    b_tree_1: TreeNode = TreeNode(1)
    b_tree_1.left = TreeNode(2)
    b_tree_1.right = TreeNode(3)
    b_tree_1.right.right = TreeNode(4)
    b_tree_1.right.left = TreeNode(5)
    b_tree_1.left.right = TreeNode(6)
    b_tree_1.left.left = TreeNode(7)

    print(f"Maximum width of b_tree_1: {iterative_max_width(b_tree_1)}")
    print("Maximum width of b_tree_1 including null nodes between leftmost & rightmost Non-null nodes:"
          f" {get_maximum_width_including_non_terminal_null_nodes(b_tree_1)}")
    print(f"Height of b_tree_1 using recursion: {recursive_max_height(b_tree_1)}")
    print(f"Height of b_tree_1 using iteration: {iterative_max_height(b_tree_1)}")

    b_tree_2: TreeNode = TreeNode(1)
    b_tree_2.left = TreeNode(2)
    b_tree_2.right = TreeNode(3)
    b_tree_2.left.left = TreeNode(4)
    b_tree_2.left.right = TreeNode(5)
    b_tree_2.right.right = TreeNode(8)
    b_tree_2.left.right.left = TreeNode(7)
    b_tree_2.left.right.right = TreeNode(6)

    print(f"Maximum width of b_tree_2: {iterative_max_width(b_tree_2)}")
    print("Maximum width of b_tree_2 including null nodes between leftmost & rightmost Non-null nodes:"
          f" {get_maximum_width_including_non_terminal_null_nodes(b_tree_2)}")
    print(f"Height of b_tree_2 using recursion: {recursive_max_height(b_tree_2)}")
    print(f"Height of b_tree_2 using iteration: {iterative_max_height(b_tree_2)}")
