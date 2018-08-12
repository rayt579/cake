'''
Given a list of integers, find the highest product you can get
from n = three of the integers.

BONUS:
1) What if we wanted the highest product of 4 items?
2) What if we wanted the highest product of k items?
3) If our highest product is really big, it could overflow. ↴ How should we protect against this?
'''

#O(n^3) time, O(1) space
def highest_n_products_bf(list_of_ints):
    max_product = 1
    for i in range(len(list_of_ints)):
        first_product = list_of_ints[i]
        for j in range(len(list_of_ints)):
            if i != j:
                second_product = first_product * list_of_ints[j]
                for k in range(len(list_of_ints)):
                    if k != i and k != j:
                        third_product = second_product * list_of_ints[k]
                        max_product = max(third_product, max_product)
    return max_product

print('Brute force method...')
print(highest_n_products_bf([5, 10, 6, 4]))
print(highest_n_products_bf([-20, 4, 15, 20]))
print(highest_n_products_bf([-10, -10, 1, 3, 2]))

# O(n log n) time, O(1) space
def highest_n_products_sort(list_of_ints):
    list_of_ints.sort()
    product = list_of_ints[len(list_of_ints) - 1]
    left_product = list_of_ints[len(list_of_ints) - 2] * list_of_ints[len(list_of_ints) - 3]
    right_product = list_of_ints[0] * list_of_ints[1]
    return product * max(left_product, right_product)

print('Sort method...')
print(highest_n_products_sort([5, 10, 6, 4]))
print(highest_n_products_sort([-20, 4, 15, 20]))
print(highest_n_products_sort([-10, -10, 1, 3, 2]))

# O(n) greedy method, O(1) space
def highest_n_products(list_of_ints):
    if len(list_of_ints) < 3:
        raise Exception('Need input <= 3')

    lowest = min(list_of_ints[0], list_of_ints[1])
    highest = max(list_of_ints[0], list_of_ints[1])
    highest_product_at_2, lowest_product_at_2 = list_of_ints[0] * list_of_ints[1], list_of_ints[0] * list_of_ints[1]
    highest_n_product = float('-inf')

    for i in range(2, len(list_of_ints)):
        highest_n_product = max(highest_product_at_2 * list_of_ints[i], lowest_product_at_2 * list_of_ints[i], highest_n_product)
        highest_product_at_2 = max(highest_product_at_2, highest * list_of_ints[i], lowest * list_of_ints[i])
        highest = max(highest, list_of_ints[i])
        lowest_product_at_2 = min(lowest_product_at_2, lowest * list_of_ints[i], highest * list_of_ints[i])
        lowest = min(lowest, list_of_ints[i])
    return highest_n_product

print('Single pass greedy method....')
print(highest_n_products([5, 10, 6, 4]))
print(highest_n_products([-20, 4, 15, 20]))
print(highest_n_products([-10, -10, 1, 3, 2]))

#SOLUTION
'''
  def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError('Less than 3 items!')

    # We're going to start at the 3rd item (at index 2)
    # so pre-populate highests and lowests based on the first 2 items.
    # We could also start these as None and check below if they're set
    # but this is arguably cleaner
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest  = min(list_of_ints[0], list_of_ints[1])
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2  = list_of_ints[0] * list_of_ints[1]

    # Except this one--we pre-populate it for the first *3* items.
    # This means in our first pass it'll check against itself, which is fine.
    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    # Walk through items, starting at index 2
    for i in xrange(2, len(list_of_ints)):
        current = list_of_ints[i]

        # Do we have a new highest product of 3?
        # It's either the current highest,
        # or the current times the highest product of two
        # or the current times the lowest product of two
        highest_product_of_3 = max(highest_product_of_3,
                                   current * highest_product_of_2,
                                   current * lowest_product_of_2)

        # Do we have a new highest product of two?
        highest_product_of_2 = max(highest_product_of_2,
                                   current * highest,
                                   current * lowest)

        # Do we have a new lowest product of two?
        lowest_product_of_2 = min(lowest_product_of_2,
                                  current * highest,
                                  current * lowest)

        # Do we have a new highest?
        highest = max(highest, current)

        # Do we have a new lowest?
        lowest = min(lowest, current)

    return highest_product_of_3
'''