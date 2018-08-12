'''
Write a recursive function for generating all
permutations of an input string. Return them as a set.

Takeaways:
    1) Ask yourself if you must mutate the string input, can use list slicing instead
    2) Draw a recursion tree on a smaller input
'''

# Exponential time, O(k) space, where k is the number of possible permutations
def permute(text):
    print('Permute: {}'.format(text))

    if len(text) == 0:
        return set(text)
    permutation_set = set()

    for letter in text:
        letter_index = text.index(letter)
        permutations = permute(text[:letter_index] + text[letter_index + 1:])
        if len(permutations) == 0:
            permutation_set.add(letter)
        else:
            for other in permutations:
                permutation_set.add(letter + other)
    return permutation_set


print('Permutations for string: {}'.format(sorted(permute('ABCA'))))
