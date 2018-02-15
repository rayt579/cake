'''
Write a function for doing an in-place shuffle of a list.
The shuffle must be uniform, meaning each item in the original list
must have the same probability of ending up in each spot in the final list.

Assume you have a function get_random(floor, ceiling) for getting a
random integer >= floor and <= ceiling.

Takeaways
1) Be prepared with an understanding of probabilities so you can prove uniformity
- Some outcomes can be more likely than others!
2) For in-place operations, use the zone pointer method.
'''

import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def naive_shuffle(original_list):
    for i in range(len(original_list) - 1):
        randindex = get_random(0, len(original_list) - 1)
        original_list[i], original_list[randindex] = original_list[randindex], original_list[i]

# O(n) time, O(1) space
def in_place_shuffle(original_list):
    for i in range(len(original_list) - 1):
        randindex = get_random(i, len(original_list) - 1)
        original_list[i], original_list[randindex] = original_list[randindex], original_list[i]


a = [1, 2, 3, 4, 5]
print(a)
print('Shuffled:')
in_place_shuffle(a)
print(a)
