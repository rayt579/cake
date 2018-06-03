'''
Write a function that merges two sorted lists into one

TAKEAWAYS:
    1) Always walk through toy examples.
    2) Always state brute force solution.
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
