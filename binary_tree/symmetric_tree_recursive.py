class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_mirror(root: TreeNode, root2: TreeNode):
    if not root and not root2:
        return True

    if not root or not root2:
        return False

    return ((root.val == root2.val)
            and is_mirror(root.right, root2.left)
            and is_mirror(root.left, root2.right))


def is_symmetric(root: TreeNode) -> bool:
    return is_mirror(root, root)


if __name__ == '__main__':
    one = TreeNode(1)
    two_one = TreeNode(2)
    two_two = TreeNode(2)
    three_one = TreeNode(3)
    three_two = TreeNode(4)
    three_three = TreeNode(4)
    three_four = TreeNode(3)

    one.left = two_one
    one.right = two_two

    two_one.left = three_one
    two_one.right = three_two

    two_two.left = three_three
    two_two.right = three_four

    result = is_symmetric(one)
    print(f'result {result}')
