class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def postorder_traversal(root, visited=[]):
    if root is None:
        return

    if root.left:
        postorder_traversal(root.left)

    if root.right:
        postorder_traversal(root.right)

    visited.append(root.val)

    return visited


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
