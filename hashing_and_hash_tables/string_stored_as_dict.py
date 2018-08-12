'''
Write a function that that takes a long string
and builds its as a dictionary, where key are words
and the values are the number of times the word occured

Keep in mind that you should be able to handle punction like
commas, as well as upper and lowercase

Takeaways:
    1) Important discussion to be had when using strings. How to handle casing and punctation?
    2) Intelligently discuss tradeoffs and clarify what path to go down.


Bonus:
1) We haven't explicitly talked about how to handle more complicated character sets. How would you make your solution work with more unicode characters? What changes need to be made to handle silly sentences like these:

I'm singing ♬ on a ☔ day.

☹ + ☕ = ☺.

2) We limited our input to letters, hyphenated words and punctuation. How would you expand your functionality to include numbers, email addresses, twitter handles, etc.?
3) How would you add functionality to identify phrases or words that belong together but aren't hyphenated? ("Fire truck" or "Interview Cake")
4) How could you improve your capitalization algorithm?
5) How would you avoid having duplicate words that are just plural or singular possessives?
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

