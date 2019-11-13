class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorder_traversal(root):
    if root is None:
        return

    stack = []
    explored = []
    node = root

    while node or stack:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        explored.append(node.val)
        node = node.right

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

    result = inorder_traversal(f)
    print(f'result {result}')
