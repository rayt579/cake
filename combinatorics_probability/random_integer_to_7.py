'''
Write a function rand7() that generates a random integer from 1 to 7
using a function rand5. You must return each integer with equal probability

Takeaways:
    1) Always ask yourself how to generate uniform distribution. We proved no power of 5 is divisible by 7.
    2) Remember the fundamental theorem of arithmetic: single prime factorization for every integer.
    3) Enumerate combinations using bases!!
'''

import random

def rand5():
    return random.randrange(1, 6)

# This will guarantee a uniform distributions, where we map 5^2 combinations to a table
# O(inf) time complexity, O(1) space
def rand7_store_results():
    results = [
            [1, 2, 3, 4, 5],
            [6, 7, 1, 2, 3],
            [4, 5, 6, 7, 1],
            [2, 3, 4, 5, 6],
            [7, 0, 0, 0, 0]]

    while True:
        i = rand5() - 1
        j = rand5() - 1
        if results[i][j] == 0:
            continue
        else:
            return results[i][j]

from collections import Counter
# Here we enumerate the combinations [1, ..., 25] using two-digit base 5.
# O(inf) time worst case, O(1) space
def rand7():
    while True:
        outcome = rand5() * 5 + rand5() - 5
        if outcome <= 21:
            if outcome % 7 == 0:
                return 7
            else:
                return outcome % 7

hundred_rolls = [rand7() for _ in range(100)]
print(Counter(hundred_rolls))

