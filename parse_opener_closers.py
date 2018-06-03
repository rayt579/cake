'''
Write an efficient function that tells us whether
an input string's openers and closers are
properly nested
'''
# O(n) time, O(n) space worst case
def is_valid_use_of_brackets(sentence):
    def expected_close_sym(sym):
        if sym == '{':
            return '}'
        elif sym == '(':
            return ')'
        elif sym == '[':
            return ']'
        else:
            raise Exception('Unknown opening symbol')

    open_symbols = ['{', '(', '[']
    closed_symbols = ['}', ')', ']']
    stack = []
    for char in sentence:
        if char in open_symbols:
            stack.append(char)
        elif char in closed_symbols:
            if len(stack) == 0:
                return False
            open_symbol = stack.pop()
            if char != expected_close_sym(open_symbol):
                return False
    return len(stack) == 0

print(is_valid_use_of_brackets("{[]()}"))
print(is_valid_use_of_brackets("{[(])}"))
print(is_valid_use_of_brackets("{[}"))
