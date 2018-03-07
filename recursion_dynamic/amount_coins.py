'''
Write a function given the amount of money
and a list of coin denominations, that computes the number of ways
to make the amount of money with coins of the available denominations

Takeaways:
    1) Draw a recursion tree if you want to use recursion.
    2) Solve subproblems when you sense a DP problem.
'''

def combinations_with_amount(amount, denominations, current_index=0):
    if amount == 0:
        return 1
    if amount < 0 or current_index == len(denominations):
        return 0

    current_coin = denominations[current_index]

    num_combinations = 0
    while amount >= 0:
        num_combinations += combinations_with_amount(amount, denominations, current_index + 1)
        amount -= current_coin

    return num_combinations

# O(n * m) time and space, where n is the amount and m is the number of denominations
combinations_at_index = {}
def combinations_with_amount_memoization(amount, denominations, current_index=0):
    memo_key = str((amount, current_index))
    if memo_key in combinations_at_index:
        return combinations_at_index[memo_key]

    if amount == 0:
        return 1
    if amount < 0 or current_index == len(denominations):
        return 0

    current_coin = denominations[current_index]

    num_combinations = 0
    while amount >= 0:
        num_combinations += combinations_with_amount(amount, denominations, current_index + 1)
        amount -= current_coin

    combinations_at_index[memo_key] = num_combinations
    return num_combinations

# O(nm) time and O(n) space, where n is the amount, and m the number of coins in the denominations
def change_combinations(final_amount, denoms):
    change_combinations = [0] * (final_amount + 1)
    change_combinations[0] = 1
    for denom in denoms:
        for amount in range(len(change_combinations)):
            if amount >= denom:
                change_combinations[amount] += change_combinations[amount - denom]

    return change_combinations[-1]

print(combinations_with_amount(4, [1,2]))
print(combinations_with_amount_memoization(4, [1,2]))
print(change_combinations(4, [1,2]))
