'''
You have a function rand7() that generates a random int from 1 to 7.
Use it to write a function rand5() that generates a random integer
from 1 to 5.

rand7() and rand5() both must return integers with equal probability

TAKEAWAYS:
    1) For math related questions, draw out working examples.
'''
import random
def rand7():
    return random.randrange(1, 8)

# To guarantee a uniform distribution, this will run in infinite time worst case. O(1) space, O(infinity) time worst case
def rand5():
    num = rand7()
    while num > 5:
        num = rand7()
    return num


def rand5_recursive():
    num = rand7()
    return num if num <= 5 else rand5_recursive()


for _ in range(100):
    print(rand5())
    print(rand5_recursive())


