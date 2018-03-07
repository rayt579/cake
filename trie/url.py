'''
Let visited be a set where I store all URLs that I have ever visited.

How can I trim down the amount of space taken up by visited?


Takeaways:
    1) Remember that tries can be implemented using something simple like a nested dictionary.
    2) Ask yourself how to take a small solution even farther.
'''

# This is a nested-dictionary implementation
class Trie(object):

    def __init__(self):
        self.root_node = {}

    def add_word(self, word):
        current_word = self.root_node
        is_new_word = False

        for char in word:
            if char not in current_word:
                is_new_word = True
                current_word[char] = {}
            current_word = current_word[char]

        if "End of Word" not in current_word:
            is_new_word = True
            current_node["End of Word"] = {}

        return is_new_word



