'''
Given a list of integers, find the highest product you can get
from n = three of the integers.

Takeaways:
    1) Greedy solution will require a lot of book keeping for a single pass. Keep this is mind.
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
