class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorder_traversal(root, visited=[]):
    if root is None:
        return

    visited.append(root.val)

    if root.left:
        preorder_traversal(root.left, visited)

    if root.right:
        preorder_traversal(root.right, visited)

    return visited


if __name__ == '__main__':
    root = TreeNode(1)
    one = TreeNode(2)
    two = TreeNode(3)
    root.right = one
    one.left = two

    result = preorder_traversal(root)
    print(f'result {result}')
