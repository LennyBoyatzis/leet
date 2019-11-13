class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def postorder_traversal(root):
    if root is None:
        return

    stack = [root]
    explored = []

    while stack:
        node = stack.pop()
        explored.append(node.val)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return explored


if __name__ == '__main__':
    f = TreeNode('F')
    b = TreeNode('B')
    g = TreeNode('G')
    a = TreeNode('A')
    d = TreeNode('D')
    c = TreeNode('C')
    e = TreeNode('E')
    i = TreeNode('I')
    h = TreeNode('H')

    f.left = b
    f.right = g

    b.left = a
    b.right = d

    d.left = c
    d.right = e

    g.right = i
    i.left = h

    result = postorder_traversal(f)
    print(f'result {result}')
