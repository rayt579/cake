'''
Write a function that takes a message and reverses
the order of the words in-place

Assume the message contains only letters and spaces


Takeaways:
    1) Get unstuck by trying to solve a simpler problem.
    2) Work to clarify problem constraints

Bonus:
    1) How would you handle punctuation?
'''

# O(n) time, O(n) space
def reverse_words(message):
    message = list(message)

    def reverse_message(start, end, message):
        while start < end:
            message[start], message[end] = message[end], message[start]
            start += 1
            end -= 1

    reverse_message(0, len(message) - 1, message)
    start = 0
    for i in range(len(message) + 1):
        if i == len(message) or message[i] == ' ':
            reverse_message(start, i - 1, message)
            start = i + 1

    return ''.join(message)

message = 'find you will pain only go you recordings security the into if'
print(reverse_words(message))
reverse_words(message)


# Solution
'''
  def reverse_words(message):
    # First we reverse all the characters in the entire message
    reverse_characters(message, 0, len(message)-1)

    # This gives us the right word order
    # but with each word backward

    # Now we'll make the words forward again
    # by reversing each word's characters

    # We hold the index of the *start* of the current word
    # as we look for the *end* of the current word
    current_word_start_index = 0

    for i in xrange(len(message) + 1):
        # Found the end of the current word!
        if (i == len(message)) or (message[i] == ' '):
            reverse_characters(message, current_word_start_index, i - 1)
            # If we haven't exhausted the message our
            # next word's start is one character ahead
            current_word_start_index = i + 1


    def reverse_characters(message, left_index, right_index):
        # Walk towards the middle, from both sides
        while left_index < right_index:
            # Swap the left char and right char
            message[left_index], message[right_index] = \
                message[right_index], message[left_index]
            left_index  += 1
            right_index -= 1
'''