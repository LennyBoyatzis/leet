from collections import namedtuple


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def subtreeWithAllDeepest(root: TreeNode) -> TreeNode:
    result = namedtuple("result", ("node", "dist"))

    def dfs(node):
        if not node:
            return result(None, 0)

        left, right = dfs(node.left), dfs(node.right)

        if left.dist > right.dist:
            return result(left.node, left.dist + 1)

        if left.dist < right.dist:
            return result(right.node, right.dist + 1)

        return result(node, left.dist + 1)

    return dfs(root).node


if __name__ == '__main__':
    one = TreeNode(3)
    two = TreeNode(5)
    three = TreeNode(1)
    four = TreeNode(6)
    five = TreeNode(2)
    six = TreeNode(0)
    seven = TreeNode(8)
    eight = TreeNode(7)
    nine = TreeNode(4)

    one.left = two
    one.right = three

    two.left = six
    two.right = five

    three.left = six
    three.right = seven

    five.left = eight
    five.right = nine

    result = subtreeWithAllDeepest(one)
    print(f'what is result {result}')
