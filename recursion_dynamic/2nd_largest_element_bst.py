'''
Write a function to find the 2nd largest element in a BST
'''
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def second_largest_element_in_bst(root):
    if not root:
        return None
    prev, curr = None, root
    while curr.right:
        prev = curr
        curr = curr.right
    if curr.left:
        curr = curr.left
        while curr.right:
            curr = curr.right
        return curr.val
    return prev.val

a = TreeNode(4)
a.right = TreeNode(20)
a.right.right = TreeNode(27)
a.right.right.right = TreeNode(30)
a.right.right.right.left = TreeNode(28)
a.right.right.right.left.right = TreeNode(29)

print('Expect 29: {}'.format(second_largest_element_in_bst(a)))
