'''
Write a function to see if a binary tree is superbalanced.

Superbalanced if the difference between the depths of any two leaf nodes is no
greater than one

TAKEAWAYS:
    1) BFS vs. DFS:
        - DFS will be height based, BFS will use tree levels.
        - BFS will find shortest path to a node.
        - DFS generally requires less memory than a BFS.
    2) Remember to keep record height of tree in tuple
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None


def is_superbalanced(root):
    if not root:
        return True
    min_depth = float('inf')
    visit = [(root, 0)]
    while len(visit) > 0:
        node, depth = visit.pop()
        if node.is_leaf():
            min_depth = min(min_depth, depth)
            if abs(min_depth - depth) > 1:
                return False
        else:
            if node.left:
                visit.append((node.left, depth + 1))
            if node.right:
                visit.append((node.right, depth + 1))
    return True

# Solution
'''
  def is_balanced(tree_root):
    # A tree with no nodes is superbalanced, since there are no leaves!
    if tree_root is None:
        return True

    # We short-circuit as soon as we find more than 2
    depths = []

    # We'll treat this list as a stack that will store tuples of (node, depth)
    nodes = []
    nodes.append((tree_root, 0))

    while len(nodes):
        # Pop a node and its depth from the top of our stack
        node, depth = nodes.pop()

        # Case: we found a leaf
        if (not node.left) and (not node.right):
            # We only care if it's a new depth
            if depth not in depths:
                depths.append(depth)

                # Two ways we might now have an unbalanced tree:
                #   1) more than 2 different leaf depths
                #   2) 2 leaf depths that are more than 1 apart
                if ((len(depths) > 2) or
                        (len(depths) == 2 and abs(depths[0] - depths[1]) > 1)):
                    return False
        else:
            # Case: this isn't a leaf - keep stepping down
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))

    return True
'''