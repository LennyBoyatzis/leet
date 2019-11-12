class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorder_traversal(root):
    if not root:
        return None

    stack = [root]
    explored = []

    while stack:
        node = stack.pop()
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

        explored.append(node.val)
    return explored


if __name__ == '__main__':
    root = TreeNode(1)
    one = TreeNode(2)
    two = TreeNode(3)
    root.right = one
    one.left = two

    result = preorder_traversal(root)
    print(f'result {result}')
