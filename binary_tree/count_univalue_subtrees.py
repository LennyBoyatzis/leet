class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def count_univalue_subtrees(root: TreeNode, count=0) -> int:
    if not root:
        return

    if not root.left or not root.right:
        return 1

    univalue = False

    if root.left and root.right:
        univalue = root.left.val == root.right.val == root.val
        count += 1
    elif root.left and not root.right:
        univalue = root.left.val == root.val
        count += 1
    elif root.right and not root.left:
        univalue = root.right.val == root.val
        count += 1

    return count_univalue_subtrees(root.left, count) + count_univalue_subtrees(root.right, count)




if __name__ == '__main__':
    one = TreeNode(5)
    two_one = TreeNode(1)
    two_two = TreeNode(5)
    three_one = TreeNode(5)
    three_two = TreeNode(5)
    three_three = TreeNode(5)

    one.left = two_one
    one.right = two_two

    two_one.left = three_one
    two_one.right = three_two

    two_two.right = three_three

    result = count_univalue_subtrees(one)
    print(f'result {result}')
