'''
Write a function that merges two sorted lists into one

TAKEAWAYS:
    1) Always walk through toy examples.
    2) Always state brute force solution.

Bonus:
    1) What if we wanted to merge several sorted lists? Write a function that takes as an input a list of sorted lists and outputs a single sorted list with all the items from each list.
    2) Do we absolutely have to allocate a new list to use for the merged output? Where else could we store our merged list? How would our function need to change?
'''

# O(n + m) time, O(n + m) space
def merge_lists(list_a, list_b):
    if not list_a or not list_b:
        raise Exception('Empty List')

    sorted_list = []
    a_index = 0
    b_index = 0

    while a_index < len(list_a) and b_index < len(list_b):
        if list_a[a_index] < list_b[b_index]:
            sorted_list.append(list_a[a_index])
            a_index += 1
        else:
            sorted_list.append(list_b[b_index])
            b_index += 1

    if a_index == len(list_a):
        while b_index < len(list_b):
            sorted_list.append(list_b[b_index])
            b_index += 1
    else:
        while a_index < len(list_a):
            sorted_list.append(list_a[a_index])
            a_index += 1

    return sorted_list

A = [1, 4, 6]
B = [1, 2, 5, 8]
print(merge_lists(A, B))

my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
print(merge_lists(my_list, alices_list))


#Solution
'''
def merge_lists(my_list, alices_list):
    # Set up our merged_list
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0
    while current_index_merged < merged_list_size:
        is_my_list_exhausted = current_index_mine >= len(my_list)
        is_alices_list_exhausted = current_index_alices >= len(alices_list)
        if (not is_my_list_exhausted and
                (is_alices_list_exhausted or
                 my_list[current_index_mine] < alices_list[current_index_alices])):
            # Case: next comes from my list
            # My list must not be exhausted, and EITHER:
            # 1) Alice's list IS exhausted, or
            # 2) the current element in my list is less
            #    than the current element in Alice's list
            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1
        else:
            # Case: next comes from Alice's list
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1

        current_index_merged += 1

    return merged_list
'''