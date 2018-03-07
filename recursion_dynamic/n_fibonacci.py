'''
Write a function fib() that takes an integer n and
returns the nth Fibonacci number

Lets say our Fibonacci series is 0-indexed and starts with 0

Takeaways:
    1) Remember bottom-up (DP) vs. top down approach (recursion)
    2) Remember that recursive calls take up stack space
'''

def fibonacci_recursive(n):
    if n < 0:
        return -1
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n_fibonacci_number = {}

def fibonacci_recursive_with_cache(n):
    if n < 0:
        return -1
    if n <= 1:
        return n
    if n not in n_fibonacci_number:
        num = fibonacci_recursive_with_cache(n - 1) + fibonacci_recursive_with_cache(n - 2)
        n_fibonacci_number[n] = num
        return num
    else:
        return n_fibonacci_number[n]

def fibonacci_bottom_up(n):
    if n < 0:
        return -1
    if n <= 1:
        return n
    prev_fib_number = 0
    n_fib_number = 1
    for i in range(1, n):
        temp = prev_fib_number + n_fib_number
        prev_fib_number = n_fib_number
        n_fib_number = temp
    return n_fib_number

for i in range(10):
    print(fibonacci_recursive(i))

print('Recursive using memoization')
for i in range(10):
    print(fibonacci_recursive_with_cache(i))

print('Bottom-up Approach')
for i in range(10):
    print(fibonacci_bottom_up(i))
