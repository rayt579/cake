'''
Write a function to tell us if a full deck of cards shuffled_deck
is a single riffle of two other halves half1 and half2

Definition of the Riffle Algorithm
------------------------------------
1) cut the deck into halves half1 and half2
2) take a random number of cards from top of half1 (can be 0) and throw them into the shuffled_deck
3) take a random number of cards from top of half2 (can be 0) and throw them into the shuffled_deck
4) repeat steps 2 and 3 until both halfs are empty

Takeaways:
    1) Work with the interviewer to break down the problem to digestable chunks. You need to understand the problem
    2) Avoid using list slicing when necessary because you incur space costs. Keep track of pointers instead.
'''

# O(n) time, O(n) space
def is_shuffled_with_single_riffle_recursive(shuffled_deck, h1, h2, shuf_index=0, h1_index=0, h2_index=0):
    if shuf_index == len(shuffled_deck):
        return True
    if h1_index < len(h1) and h1[h1_index] == shuffled_deck[shuf_index]:
        return is_shuffled_with_single_riffle_recursive(shuffled_deck, h1, h2, shuf_index + 1, h1_index + 1, h2_index)
    elif h2_index < len(h2) and h2[h2_index] == shuffled_deck[shuf_index]:
        return is_shuffled_with_single_riffle_recursive(shuffled_deck, h1, h2, shuf_index + 1, h1_index, h2_index + 1)
    else:
        return False

# O(n) time, O(n) space
def is_shuffled_with_single_riffle(shuffled_deck, half1, half2):
    h1_index = 0
    h2_index = 0
    for i in range(len(shuffled_deck)):
        if h1_index < len(half1) and shuffled_deck[i] == h1[h1_index]:
            h1_index += 1
        elif h2_index < len(half2) and shuffled_deck[i] == h2[h2_index]:
            h2_index += 1
        else:
            return False
    return True

shuffled_with_riffle = [10, 4, 5, 1]
shuffled_without_riffle = [10, 4, 5, 9]
h1 = [10, 4, 1]
h2 = [5]

print(is_shuffled_with_single_riffle_recursive(shuffled_with_riffle, h1, h2))
print(is_shuffled_with_single_riffle(shuffled_with_riffle, h1, h2))

print(is_shuffled_with_single_riffle_recursive(shuffled_without_riffle, h1, h2))
print(is_shuffled_with_single_riffle(shuffled_without_riffle, h1, h2))
