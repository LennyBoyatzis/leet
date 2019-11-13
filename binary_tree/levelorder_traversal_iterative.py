from collections import deque


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelorder_traversal(root):
    if root is None:
        return

    queue = deque([root])
    depth = 0
    levels = []

    while queue:
        levels.append([])
        level_length = len(queue)

        for i in range(level_length):
            node = queue.popleft()
            levels[depth].append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        depth += 1
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
