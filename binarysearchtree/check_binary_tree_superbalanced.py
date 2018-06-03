'''
Write a function to see if a binary tree is superbalanced

A tree is superbalanced if the difference between the depths of any
two leaf nodes is no greater than one.

Takeaways:
    1) Keep in mind direction you are moving down with the tree.
    In the linear approach, we move from top down, caching the height.
'''

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self,value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def is_superbalanced_tree(root):
    nodes_to_visit = [(root, 0)]
    minimum_depth = float('inf')

    while len(nodes_to_visit) > 0:
        node, depth = nodes_to_visit.pop()
        if not node.right and not node.left:
            if minimum_depth != float('inf'):
                if abs(depth - minimum_depth) > 1:
                    return False
            minimum_depth = min(minimum_depth, depth)
        else:
            if node.right:
                nodes_to_visit.append((node.right, depth + 1))
            if node.left:
                nodes_to_visit.append((node.left, depth + 1))

    return True

a = BinaryTreeNode(1)
a.left = BinaryTreeNode(2)
a.left.left = BinaryTreeNode(3)
a.left.right = BinaryTreeNode(4)
a.left.right.right = BinaryTreeNode(5)
a.right = BinaryTreeNode(6)
a.right.left = BinaryTreeNode(7)
a.right.left.right = BinaryTreeNode(8)
a.right.right = BinaryTreeNode(9)
a.right.right.right = BinaryTreeNode(10)
a.right.right.right.right = BinaryTreeNode(10)

print('Expecting False: {}'.format(is_superbalanced_tree(a)))

a = BinaryTreeNode(1)
a.left = BinaryTreeNode(2)
a.left.left = BinaryTreeNode(3)
a.left.left.left = BinaryTreeNode(2)
a.left.right = BinaryTreeNode(4)
a.left.right.right = BinaryTreeNode(5)
a.right = BinaryTreeNode(6)
a.right.left = BinaryTreeNode(7)
a.right.left.right = BinaryTreeNode(8)
a.right.right = BinaryTreeNode(9)
a.right.right.right = BinaryTreeNode(10)
a.right.right.right.right = BinaryTreeNode(10)

print('Expecting True: {}'.format(is_superbalanced_tree(a)))
