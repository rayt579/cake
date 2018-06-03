'''
Write a function that that takes a long string
and builds its as a dictionary, where key are words
and the values are the number of times the word occured

Keep in mind that you should be able to handle punction like
commas, as well as upper and lowercase

Takeaways:
    1) Important discussion to be had when using strings. How to handle casing and punctation?
    2) Discuss tradeoffs and clarify what path to go down.
'''

class WordCloudData(object):
    def __init__(self):
        self.word_counts = {}

    # O(n) time, O(n) space
    def build_count_table(self, text):
        current_word_length = 0
        current_word_index = 0
        for i, character in enumerate(text):
            if i == len(text) - 1 and character == '.':
                self.add_word(text[current_word_index:current_word_index + current_word_length])
            elif character == ' ' and current_word_length > 0:
                self.add_word(text[current_word_index:current_word_index + current_word_length])
                current_word_length = 0
            elif character.isalpha():
                if current_word_length == 0:
                    current_word_index = i
                current_word_length += 1

    def add_word(self, word):
        if word in self.word_counts:
            self.word_counts[word] += 1
        elif word.lower() in self.word_counts:
            self.word_counts[word.lower()] += 1
        elif word.capitalize() in self.word_counts:
            self.word_counts[word] = 1
            self.word_counts[word] += self.word_counts[word.capitalize()]
            del self.word_counts[word.capitalize()]
        else:
            self.word_counts[word] = 1

word = WordCloudData()
word.build_count_table('Cliff finished his cake and paid the bill. Bill finished his cake at the edge of the cliff.')
print(word.word_counts)

