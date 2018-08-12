'''
Write a function for reversing a linked list. Do it in-place.

Your function will have one input: the head of the list
Your function will return the new head of the list


TAKEAWAY: Pay attention to order of operations.
Make sure your code is tested against hand-drawn inputs
'''

class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time, O(n) space complexity
def reverse_list_recursive(head):
    if head is None:
        return None
    if head.next is None:
        return head
    rest = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return rest

# O(n) time, O(1) space
def reverse_list_iterative(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    head.next = None
    return prev

mylist = LinkedListNode('a')
mylist.next = LinkedListNode('b')
mylist.next.next = LinkedListNode('c')
mylist.next.next.next = LinkedListNode('d')

print('Original list:')
curr = mylist
while curr:
    print(curr.value)
    curr = curr.next

print('Revesed recursively:')
recurse = reverse_list_recursive(mylist)
curr = recurse
while curr:
    print(curr.value)
    curr = curr.next

mylist = LinkedListNode('a')
mylist.next = LinkedListNode('b')
mylist.next.next = LinkedListNode('c')
mylist.next.next.next = LinkedListNode('d')

print('Revesed iteratively:')
iterative = reverse_list_iterative(mylist)
curr = iterative
while curr:
    print(curr.value)
    curr = curr.next
