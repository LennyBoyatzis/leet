class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorder_traversal(root, visited=[]):
    if root is None:
        return

    if root.left:
        inorder_traversal(root.left)

    visited.append(root.val)

    if root.right:
        inorder_traversal(root.right)

    return visited


if __name__ == '__main__':
    root = TreeNode(1)
    one = TreeNode(2)
    two = TreeNode(3)
    root.right = one
    one.left = two

    result = inorder_traversal(root)
    print(f'result {result}')
