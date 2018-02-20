'''
Check if singly-linked list has a cycle.

A cycle occurs when a node's next points back to a previous node in the list.

Takeaways:
    1) Prove that the fast runner will never overtake the slow runner
    using proof by contradiction
'''


class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time, O(n) space
def contains_cycle_using_set(head):
    visited_nodes = set()
    while head:
        if head in visited_nodes:
            return True
        visited_nodes.add(head)
        head = head.next
    return False

# O(n) time, O(1) space
def contains_cycle(head):
    slow_runner = head
    fast_runner = head

    while fast_runner and fast_runner.next:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        if slow_runner is fast_runner:
            return True
    return False

no_cycle = LinkedListNode(1)
no_cycle.next = LinkedListNode(2)
no_cycle.next.next = LinkedListNode(3)

cycle_at_end = LinkedListNode(1)
cycle_at_end.next = LinkedListNode(2)
cycle_at_end.next.next = cycle_at_end.next

print('Expecting no cycle, contains_cycle returns: {}'.format(contains_cycle(no_cycle)))
print('Expecting cycle, contains_cycle returns: {}'.format(contains_cycle(cycle_at_end)))

