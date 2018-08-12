'''
Write a function to reverse a string in-place.

TAKEAWAYS
1) Strings in Python are immutable (no such thing as in-place reverse), don't forget this or you will embarass yourself.
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



#Solution
'''
  def reverse(list_of_chars):

    left_index  = 0
    right_index = len(list_of_chars) - 1

    while left_index < right_index:
        # Swap characters
        list_of_chars[left_index], list_of_chars[right_index] = \
            list_of_chars[right_index], list_of_chars[left_index]
        # Move towards middle
        left_index  += 1
        right_index -= 1
'''