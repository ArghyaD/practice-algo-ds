from typing import Optional, List


class BinaryTreeNode:
    def __init__(self, data: Optional[int], left=None, right=None):
        self.data: int = data
        self.left: Optional[BinaryTreeNode] = left
        self.right: Optional[BinaryTreeNode] = right
        self.next_right: Optional[BinaryTreeNode] = None


def connect_nodes_at_same_level(root: Optional[BinaryTreeNode]):
    queue: List[BinaryTreeNode] = [root] if root else []

    while queue:
        size: int = len(queue)
        prev_node: BinaryTreeNode = BinaryTreeNode(None)
        count = 0
        while count < size:
            temp: BinaryTreeNode = queue.pop(0)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

            prev_node.next_right = temp
            prev_node = temp
            count += 1


def level_order_traversal(root: Optional[BinaryTreeNode]):
    queue: List[BinaryTreeNode] = [root] if root else []

    while queue:
        size: int = len(queue)
        count = 0
        while count < size:
            temp: BinaryTreeNode = queue.pop(0)
            next_right: Optional[int] = temp.next_right.data if temp.next_right else None
            print(f"{temp.data}({next_right})", end=" ")
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            count += 1
        print()


if __name__ == '__main__':
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.right.left = BinaryTreeNode(5)
    root.right.right = BinaryTreeNode(6)

    connect_nodes_at_same_level(root)

    level_order_traversal(root)
