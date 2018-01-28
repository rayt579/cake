'''
Write a function that takes an integer k and
the head node of a singly-linked list, and returns the kth to last node
in the list.

TAKEAWAYS:
    1) Think about what happens when size of inputs change, i.e n >> k
    2) Consider optimizations from the processor (LRU)
'''

class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n + m), where n is length of list and m is (length - k)
def kth_to_last_node_bf(k, head):
    curr = head
    length = 0
    while curr:
        length += 1
        curr = curr.next

    target_index = length - k
    index = 0
    curr = head
    while curr:
        if index == target_index:
            return curr
        index += 1
        curr = curr.next
    return None

def kth_to_last_node_sliding(k, head):
    if k < 1:
        raise ValueError('Impossible to find less than the first to last node')
    left_node, right_node = head, head
    for _ in range(k - 1):
        right_node = right_node.next
        if right_node is None:
            raise ValueError('k is greater than the size of the linked list')

    while right_node.next:
        left_node = left_node.next
        right_node = right_node.next
    return left_node

mylist = LinkedListNode('AngelFood')
mylist.next = LinkedListNode('Bundt')
mylist.next.next = LinkedListNode('Cheese')
mylist.next.next.next = LinkedListNode('Devils Food')
mylist.next.next.next.next = LinkedListNode('Eccles')

print('Two-pass method')
for i in range(5, 0, -1):
    print(kth_to_last_node_bf(i, mylist).value)

print('Sliding window method')
for i in range(5, 0, -1):
    print(kth_to_last_node_sliding(i, mylist).value)
