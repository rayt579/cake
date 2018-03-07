'''
Implement a new class MaxStack with a method get_max()
that returns the largest element in the stack.

TAKEAWAYS:
    1) Look for what you need to optimize, clarify with your interviewer
'''

# O(1) time for push(), pop(), get_max()
# O(m) space, where m is the number of total operations performed on the stack
class MaxStack(object):
    def __init__(self):
        self.items = []
        self.maxes_stack = []

    def push(self, item):
        self.items.append(item)

        if not self.maxes_stack or item >= self.maxes_stack[-1]:
            self.maxes_stack.append(item)

    def pop(self):
        if not self.items:
            raise Exception('Empty stack!')
        item = self.items.pop()
        if item == self.maxes_stack[-1]:
            self.maxes_stack.pop()

    def get_max(self):
        if not self.items:
            raise Exception('Empty stack')

        return self.maxes_stack[-1]

    def peek(self):
        if not self.items:
            raise Exception('Empty stack!')
        return self.items[-1]


stack = MaxStack()
stack.push(2)
stack.push(8)
stack.push(4)
stack.push(5)

for _ in range(4):
    print(stack.get_max())
    stack.pop()

