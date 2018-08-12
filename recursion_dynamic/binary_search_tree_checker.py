'''
Write a function to check that a binary tree is a valid binary search tree
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def is_valid_bst(self, root):
        if not root:
            return True
        visit = [(root, float('-inf'), float('inf'))]
        while len(visit) > 0:
            node, min_val, max_val = visit.pop()
            if not min_val < node.val < max_val:
                return False
            if node.left:
                visit.append((node.left, min_val, node.val))
            if node.right:
                visit.append((node.right, node.val, max_val))
        return True


