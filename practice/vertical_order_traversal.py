
from collections import deque, defaultdict


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class VerticalOrderTraversal:
    def solution(self, root: TreeNode):
        current = root

        store = defaultdict(list)
        min_d = float('inf')
        max_d = float('-inf')

        queue = deque([(0, current)])

        while queue:
            data = queue.popleft()
            store[data[0]].append(data[1])

            if data[1].left:
                queue.append((data[0] - 1, data[1].left))

            if data[1].right:
                queue.append((data[0] + 1, data[1].right))

            min_d = min(min_d, data[0])
            max_d = max(max_d, data[0])

        for i in range(int(min_d), int(max_d)+1):
            for each in store[i]:
                print(each.data)

if __name__ == '__main__':
    tree = TreeNode(
        data=5,
        left=TreeNode(
            data=3,
            left=TreeNode(1),
            right=TreeNode(4)
        ),
        right=TreeNode(
            data=9,
            left=TreeNode(6),
            right=TreeNode(11)
        )
    )

    obj = VerticalOrderTraversal()
    obj.solution(tree)
