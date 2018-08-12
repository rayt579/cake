'''
Write a function for doing an in-place shuffle of a list.
The shuffle must be uniform, meaning each item in the original list
must have the same probability of ending up in each spot in the final list.

Assume you have a function get_random(floor, ceiling) for getting a
random integer >= floor and <= ceiling.

Takeaways
1) Be prepared with an understanding of probabilities so you can prove uniformity
- Some outcomes can be more likely than others!
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



# Solution
import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def shuffle(the_list):
    # If it's 1 or 0 items, just return
    if len(the_list) <= 1:
        return the_list

    last_index_in_the_list = len(the_list) - 1

    # Walk through from beginning to end
    for index_we_are_choosing_for in xrange(0, len(the_list) - 1):

        # Choose a random not-yet-placed item to place there
        # (could also be the item currently in that spot)
        # Must be an item AFTER the current item, because the stuff
        # before has all already been placed
        random_choice_index = get_random(index_we_are_choosing_for,
                                         last_index_in_the_list)

        # Place our random choice in the spot by swapping
        if random_choice_index != index_we_are_choosing_for:
            the_list[index_we_are_choosing_for], the_list[random_choice_index] = \
                the_list[random_choice_index], the_list[index_we_are_choosing_for]