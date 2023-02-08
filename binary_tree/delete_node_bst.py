from typing import Optional, List


class TreeNode:
    def __init__(self, data: int, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def get_inorder_predecessor(root: Optional[TreeNode]):
    inorder_predecessor: Optional[TreeNode] = root.left if root else None
    prev = None
    while inorder_predecessor.right:
        prev = inorder_predecessor
        inorder_predecessor = inorder_predecessor.right
    prev.right = None
    return inorder_predecessor


def delete_node_bst(root: Optional[TreeNode], key: int):
    current: Optional[TreeNode] = root
    prev = root
    while current:
        if current.data < key:
            prev = current
            current = current.right
        elif current.data > key:
            prev = current
            current = current.left
        else:
            if not current.left:
                node_to_store = current.right
            else:
                node_to_store = get_inorder_predecessor(current)

            if prev.data < key:
                prev.right = node_to_store
            elif prev.data > key:
                prev.left = node_to_store
            else:
                prev.data = node_to_store.data
            break

def inorder_traversal(root: Optional[TreeNode]):
    current: Optional[TreeNode] = root
    stack: List[TreeNode] = []

    while current or stack:
        if current:
            stack.append(current)

            current = current.left
        else:
            current = stack.pop()

            print(current.data, end=" ")

            current = current.right


if __name__ == '__main__':

    """
    Sample Tree: 
         10        
        /   \        
       7     15    
      / \   / \    
      5 8  11 18    
    """
    root = TreeNode(10)
    root.left = TreeNode(7)
    root.right = TreeNode(15)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(11)
    root.right.right = TreeNode(18)

    print("Initial BST: ")
    inorder_traversal(root)

    # Deleting Node: 11
    node_to_delete: int = 11
    delete_node_bst(root, node_to_delete)
    print(f"\nAfter deleting {node_to_delete}: ")
    inorder_traversal(root)

    # Deleting Node: 15
    node_to_delete: int = 15
    delete_node_bst(root, node_to_delete)
    print(f"\nAfter deleting {node_to_delete}: ")
    inorder_traversal(root)

    # Deleting Node: 10
    node_to_delete: int = 10
    delete_node_bst(root, node_to_delete)
    print(f"\nAfter deleting {node_to_delete}: ")
    inorder_traversal(root)
