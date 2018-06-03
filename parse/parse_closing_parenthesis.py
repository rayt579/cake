'''
Given a sentence along with the position of an opening
parenthesis, find the corresponding closing parenthesis position

Takeaways:
    1) Think about using a stack for these problems
'''

def find_closing_parenthesis_position(sentence, open_pos):
    open_count = 0
    for i in range(open_pos + 1):
        if sentence[i] == '(':
            open_count += 1
    for i in range(len(sentence) - 1, -1, -1):
        if  sentence[i] == ')':
            open_count -= 1
            if open_count == 0:
                return i
    return -1

sentence = 'sometimes (when i nest them (my parentheticals) too much (list this (and this))) they get confusing.'
print(find_closing_parenthesis_position(sentence, 10))
