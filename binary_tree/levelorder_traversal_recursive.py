class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelorder_traversal(root, levels=[], depth=0):
    if root is None:
        return

    if len(levels) == depth:
        levels.append([])

    levels[depth].append(root.val)

    if root.left:
        levelorder_traversal(root.left, levels, depth=depth+1)

    if root.right:
        levelorder_traversal(root.right, levels, depth=depth+1)

    return levels


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

    result = levelorder_traversal(f)
    print(f'result {result}')
