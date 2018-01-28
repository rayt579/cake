'''
Write a function that, given 1) an amount of money 2) a list of coin
denominations.

computes the number of ways to make the amount of money with coins of the
available denominations.
'''

def change_possibilities_topdown(amount_left, denominations, current_index=0):
    #print('Stack Frame **** amount: {}, denominations: {}, current_index: {}'.format(amount_left, denominations, current_index))
    # we hit the amount spot on.
    if amount_left == 0:
        return 1

    # we overshot the amount left
    if amount_left < 0:
        return 0

    # we're out of denominations
    if current_index == len(denominations):
        return 0

    print('Checking ways to make {} with {}'.format(amount_left, denominations[current_index:]))

    # choose a current coin
    current_coin = denominations[current_index]

    # see how many possibilities we can get for each number of times to use current coin
    num_possibilities = 0
    while amount_left >= 0:
        num_possibilities += change_possibilities_topdown(amount_left, denominations, current_index + 1)
        amount_left -= current_coin

    return num_possibilities

print(change_possibilities_topdown(4, [1, 2, 3]));
