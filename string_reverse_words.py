'''
Write a function that takes a message and reverses
the order of the words in-place

Assume the message contains only letters and spaces


Takeaways:
    1) Get unstuck by trying to solve a simpler problem.
    2) Work to clarify problem constraints
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
