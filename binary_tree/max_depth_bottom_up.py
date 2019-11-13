class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def max_depth(root: TreeNode) -> int:
    if not root:
        return 0

    left = max_depth(root.left)
    right = max_depth(root.right)

    return max(left, right) + 1


if __name__ == '__main__':
    three = TreeNode(3)
    nine = TreeNode(9)
    twenty = TreeNode(20)
    fifteen = TreeNode(15)
    seven = TreeNode(7)

    three.left = nine
    three.right = twenty

    twenty.left = fifteen
    twenty.right = seven

    result = max_depth(three)
    print(f'result {result}')
