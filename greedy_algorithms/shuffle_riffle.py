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
    1) Work with the interviewer to break down the problem to digestable chunks. You need to understand the problem.
        - Problems can be reduced to fundamental data structures! This is just an array problem.
    2) Avoid using list slicing when necessary because you incur space costs. Keep track of pointers instead.

Bonus:
    1) This assumes shuffled_deck contains all 52 cards. What if we can't trust this (e.g. some cards are being secretly removed by the shuffle)?
    2) This assumes each number in shuffled_deck is unique. How can we adapt this to rifling lists of random integers with potential repeats?
    3) Our solution returns True if you just cut the deck—take one half and put it on top of the other. While that technically meets the definition of a riffle, what if you wanted to ensure that some mixing of the two halves occurred?
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


#Solution
'''
  def is_single_riffle(half1, half2, shuffled_deck):
    half1_index = 0
    half2_index = 0
    half1_max_index = len(half1) - 1
    half2_max_index = len(half2) - 1

    for card in shuffled_deck:
        # If we still have cards in half1
        # and the "top" card in half1 is the same
        # as the top card in shuffled_deck
        if half1_index <= half1_max_index and card == half1[half1_index]:
            half1_index += 1

        # If we still have cards in half2
        # and the "top" card in half2 is the same
        # as the top card in shuffled_deck
        elif half2_index <= half2_max_index and card == half2[half2_index]:
            half2_index += 1

        # If the top card in shuffled_deck doesn't match the top
        # card in half1 or half2, this isn't a single riffle.
        else:
            return False

    # All cards in shuffled_deck have been "accounted for"
    # so this is a single riffle!
    return True
'''