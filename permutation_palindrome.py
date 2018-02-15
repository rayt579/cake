'''
Write an efficient function that checks whether
any permutation of an input string is a palindrome

Takeaways:
    1) GOTO dict if you need to store counts of anything
    2) Use sets like a dictionary.
    3) Consider the bounds of time costs, and whether they can be reduced to O(1)
'''
# O(n) time complexity, O(k) -> O(1) space where k is the number of ASCII chars available
def is_permutation_palindrome(text):
    unused_words = set()
    for char in text:
        if char not in unused_words:
            unused_words.add(char)
        else:
            unused_words.remove(char)
    return len(unused_words) == 0 or len(unused_words) == 1

print(is_permutation_palindrome('civic'))
print(is_permutation_palindrome('ivicc'))
print(is_permutation_palindrome('civil'))
print(is_permutation_palindrome('livci'))
