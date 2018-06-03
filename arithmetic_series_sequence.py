'''
List of n + 1 numbers. Every number in the range 1...n appears once
except for one number that appears twice.

Write a function for finding the number that appears twice.


Takeaways:
    1) Remember your arithmetic series is based off triangular numbers.
    2) Watch out for overflow!
'''

def find_number_that_appears_twice(numbers):
    total = 0
    for number in numbers:
        total += number
    n = len(numbers) - 1
    return total - (n ** 2 + n) // 2



