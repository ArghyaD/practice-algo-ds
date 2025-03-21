from typing import Optional, List


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.value: int = data
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


def second_largest_in_bst(root: Optional[TreeNode]) -> int:
    current = root
    largest, buffer = right_most_node(current, True)

    if largest.left:
        second_largest = right_most_node(largest.left)
        return second_largest.value
    return buffer.pop().value


def right_most_node(root: Optional[TreeNode], store_in_buffer: bool = False):
    current: Optional[TreeNode] = root
    buffer: List[TreeNode] = []
    while current.right:
        if store_in_buffer:
            buffer.append(current)
        current = current.right
    return current if not store_in_buffer else (current, buffer)


if __name__ == "__main__":
    root = TreeNode(
        7,
        right=TreeNode(
            20,
            left=TreeNode(
                13,
                right=TreeNode(
                    17,
                    left=TreeNode(14, right=TreeNode(26)),
                    right=TreeNode(19, left=TreeNode(18)))
            )
        )
    )
    print(second_largest_in_bst(root))