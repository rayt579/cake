'''
Write a function fib() that takes an integer n and
returns the nth Fibonacci number

Lets say our Fibonacci series is 0-indexed and starts with 0
'''

def fibonacci_recursive(n):
    if n < 0:
        return -1
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_recursive_with_cache(n):


for i in range(10):
    print(fibonacci_recursive(i))
