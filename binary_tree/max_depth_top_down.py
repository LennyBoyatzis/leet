class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


answer = 0


def max_depth(root: TreeNode, depth=1) -> int:
    global answer

    if not root:
        return

    if not root.left or not root.right:
        answer = max(answer, depth)

    max_depth(root.left, depth + 1)
    max_depth(root.right, depth + 1)

    return answer


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
