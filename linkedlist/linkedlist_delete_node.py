'''
Delete a node from a singly-linked list, given only
a variable pointing to that node

Takeaways:
    1) Acknowledge imperfect solutions and be able to measure their impact
'''

class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# O(1) time and space.
# Side effect: any code that references nextnode will be referencing None
# Also, traversal breaks!
def delete_node(node):
    nextnode = node.next
    if nextnode is None:
        node.value = None
    else:
        node.value = nextnode.value
        node.next = nextnode.next

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
a.next = b
b.next = c

delete_node(c)
while a:
    print(a.value)
    a = a.next
