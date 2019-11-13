class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def has_path_sum(root: TreeNode, total: int, progress=0) -> bool:
    if not root:
        return

    if not root.left and not root.right:
        return total == progress + root.val

    progress = progress + root.val

    return (has_path_sum(root.left, total, progress)
            or has_path_sum(root.right, total, progress))


if __name__ == '__main__':
    one = TreeNode(5)
    two_one = TreeNode(4)
    two_two = TreeNode(8)
    three_one = TreeNode(11)
    three_two = TreeNode(13)
    three_three = TreeNode(4)
    four_one = TreeNode(7)
    four_two = TreeNode(2)
    four_three = TreeNode(1)

    one.left = two_one
    one.right = two_two

    two_one.left = three_one

    two_two.left = three_two
    two_two.right = three_three

    three_one.left = four_one
    three_one.right = four_two

    three_three.right = four_three

    target_sum = 22
    result = has_path_sum(one, target_sum)
    print(f'result {result}')
