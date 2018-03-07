'''
Write a function to find the 2nd largest element in a BST

Takeaways:
    1) Remember time complexities for balancing trees is O(h),
        and that h = log(n) for balanced tree, else n.
    2) Draw out examples for BST
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


# O(h) time, where h is the height of the tree, O(1) space
def get_second_largest(root):
    if root is None or (root.left is None and root.right is None):
        raise Exception('Need at least two nodes!')

    largest_node = root
    while largest_node.right:
        largest_node = largest_node.right

    if largest_node.left:
        second_largest_node = largest_node.left
        while second_largest_node.right:
            second_largest_node = second_largest_node.right
    else:
        second_largest_node = root
        while second_largest_node.right != largest_node:
            second_largest_node = second_largest_node.right

    return second_largest_node.value


a = BinaryTreeNode(1)
a.insert_right(5)
a.right.insert_left(2)
a.right.left.insert_right(4)

print(get_second_largest(a))
