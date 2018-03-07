'''
Write a function to reverse a string in-place.

TAKEAWAYS
1) Strings in Python are immutable, don't forget this or you will embarass yourself.
2) String encodings matter! Brush up on this
'''
# O(n) time, O(n) space
def string_reverse_recursion(text):
    if len(text) == 1:
        return text
    last_index = len(text) - 1
    return text[last_index] + string_reverse_recursion(text[:last_index])

# O(n) time, O(1) space
def string_reverse_bidirection(text):
    text = list(text)
    start, end =  0, len(text) - 1
    while start < end:
        text[start], text[end] = text[end], text[start]
        start += 1
        end -= 1
    return ''.join(text)

# O(n), won't really use this
def string_reverse_pythonic(text):
    return text[::-1]

original = 'original'
print(string_reverse_pythonic(original))
print(string_reverse_recursion(original))
print(string_reverse_bidirection(original))
