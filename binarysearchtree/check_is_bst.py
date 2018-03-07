'''
Write a function to check that a binary tree
is a BST.

Takeaways:
    1) Check with the interviewer before you commit to writing code
    2) Rememeber DFS is generally more space efficient than BFS, O(log n) space for balanced tree.
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

# O(n) time, O(h) space
def is_bst(root):
    visited_nodes_stack = [(root, float('-inf'), float('inf'))]
    while len(visited_nodes_stack) > 0:
        current_node, lower_bound, upper_bound = visited_nodes_stack.pop()
        if not lower_bound < current_node.value < upper_bound:
            return False
        if current_node.left:
            visited_nodes_stack.append((current_node.left, lower_bound, current_node.value))
        if current_node.right:
            visited_nodes_stack.append((current_node.right, current_node.value, upper_bound))
    return True

def is_bst_recursive(root, lower_bound, upper_bound):
    if root is None:
        return True
    if not lower_bound < root.value < upper_bound:
        return False
    return is_bst_recursive(root.left, lower_bound, root.value) and is_bst_recursive(root.right, root.value, upper_bound)


a = BinaryTreeNode(40)
a.insert_left(20)
a.left.insert_left(10)
a.left.insert_right(50)

b = BinaryTreeNode(40)
b.insert_left(20)
b.left.insert_left(10)
b.left.insert_right(25)

print('Expecting False: {}'.format(is_bst(a)))
print('Expecting True: {}'.format(is_bst(b)))

print('Recursive solution')
print('Expecting False: {}'.format(is_bst_recursive(a, float('-inf'), float('inf'))))
print('Expecting True: {}'.format(is_bst_recursive(b, float('-inf'), float('inf'))))



