'''
Given a list of IDs, which contain many duplicate integers
and one unique integer, find the unique integer
'''

# O(n) time, O(1) space
def find_unique_in_duplicate_array(delivery_id_confirmations):
    x = 0
    for num in delivery_id_confirmations:
        x ^= num
    return x

print(find_unique_in_duplicate_array([5, 3, 8, 3, 5]))
