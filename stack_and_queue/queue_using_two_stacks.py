'''
Implement a queue (enqueue and dequeue method)
using two stacks.

Optimize for the time cost of m calls on your queue.

Takeaways:
    1) Look at the cost of m calls, time complexity per item
'''

# O(m) runtime for m calls!
class Queue(object):
    def __init__(self):
        self.front = []
        self.back = []

    def enqueue(self, value):
        self.back.append(value)

    def dequeue(self):
        if not self.front and not self.back:
            raise Exception('Empty queue!')
        if not self.front:
            while self.back:
                self.front.append(self.back.pop())
        return self.front.pop()

q = Queue()
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
for _ in range(3):
    print(q.dequeue())

