'''
A building has 100 floors. One of the floors is the highest floor an egg can
be dropped from without breaking.

Given two eggs, find the highest floor an egg can be dropped without breaking,
with as few drops as possible.



Solution:
    1) We want to skip as few floors as possible on the first egg drop
    2) As we move up we want to skip one less floor.

Say we want to initially skip n floors...

n, (n-1), (n-2), (n-3), ... , 1

n(n + 1) / 2 = 100
=> n = 14

so initially skip 14, 13, 12, 11, 10, ... , 1

CASE1: With floors [0, 99], where best floor is at 98
egg1 dropped on [14, 27, 39, 50, 60, 69, 77, 83, 88, 92, 95, 97, 98]
egg2 dropped on [99]


CASE2: With floors [0, 99], where best floor is at 13
egg1 dropped on [14]
egg2 dropped on [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


This gives a worst case of 14 drops!!!!!!

Takeaways:
    1) Work through example on paper, identify bottlenecks (increasing worst case drops when egg doesn't break)
'''


