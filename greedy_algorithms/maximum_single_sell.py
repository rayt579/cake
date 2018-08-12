'''
Write an efficient function take stock_prices and returns
the best profit from 1 purchase and 1 sell.

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
get_max_profit(stock_prices_yesterday)



TAKEAWAYS:
1) Try greedy approach: saving the best answer, and what you will
need to do so.
2) Do proper housekeeping. Try negative cases.
3) 1D usually has option for divide and conquer, but may not be space efficient.
'''

# O(n^2) time, O(1) space
def get_max_profit_brute_force(stock_prices_yesterday):
    max_profit = float('-inf')
    for i in range(len(stock_prices_yesterday)):
        for j in range(i, len(stock_prices_yesterday)):
            profit = stock_prices_yesterday[j] - stock_prices_yesterday[i]
            max_profit = max(max_profit, profit)

    return max_profit

A = [10, 7, 5, 8, 11, 9]
print('Trying brute force method....')
print(get_max_profit_brute_force(A))

# T(N) = 2 T(N/2) + O(N) => O (n log n) time, O(log n) space
def get_max_profit_divide_and_conquer(stock_prices_yesterday):
    n = len(stock_prices_yesterday)
    if n == 1:
        return 0
    left = stock_prices_yesterday[:n//2]
    right = stock_prices_yesterday[n//2:]
    left_profit = get_max_profit_divide_and_conquer(left)
    right_profit = get_max_profit_divide_and_conquer(right)
    cross_profit = max(right) - min(left)

    return max(left_profit, right_profit, cross_profit)

import collections

# T(N) = T(N / 2) + O(1) => O(n) time, O(log n) space
def get_max_profit_divide_and_conquer_optimized(stock_prices_yesterday):

    ProfitWithMaxMin = collections.namedtuple('ProfitWithMaxMin', ('profit', 'min_price', 'max_price',))

    def _get_max_profit(stock_prices_yesterday, min_price, max_price):
        n = len(stock_prices_yesterday)
        if n == 1:
            return ProfitWithMaxMin(float('-inf'), stock_prices_yesterday[0], stock_prices_yesterday[0])
        left = stock_prices_yesterday[:n//2]
        right = stock_prices_yesterday[n//2:]

        left_profit_with_max_min = _get_max_profit(left, min_price, max_price)
        right_profit_with_max_min = _get_max_profit(right, min_price, max_price)

        profit = max(left_profit_with_max_min.profit, right_profit_with_max_min.profit,
                right_profit_with_max_min.max_price - left_profit_with_max_min.min_price)
        min_value = min(left_profit_with_max_min.min_price, right_profit_with_max_min.min_price)
        max_value = max(left_profit_with_max_min.max_price, right_profit_with_max_min.max_price)

        return ProfitWithMaxMin(profit, min_value, max_value)

    return _get_max_profit(stock_prices_yesterday, float('inf'), float('-inf')).profit

A = [10, 7, 5, 8, 11, 9]
print('Trying optimized divide and conquer method with ideal....')
print(get_max_profit_divide_and_conquer_optimized(A))
print('Trying optimized divide and conquer method with all negative profit...')
print(get_max_profit_divide_and_conquer_optimized([10, 9, 8, 7, 6, 5]))


# O(n) time, O(1) space
def get_max_profit_best(stock_prices_yesterday):
    min_price = stock_prices_yesterday[0]
    max_profit = float('-inf')
    n = len(stock_prices_yesterday)

    for i in range(1, n):
        max_profit = max(max_profit, stock_prices_yesterday[i] - min_price)
        min_price = min(min_price, stock_prices_yesterday[i])

    return max_profit

A = [10, 7, 5, 8, 11, 9]
print('Trying greedy method with ideal....')
print(get_max_profit_best(A))
print('Trying greedy method with all negative profit...')
print(get_max_profit_best([10, 9, 8, 7, 6, 5]))

# Solution
'''
  def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    # We'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price  = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    # Start at the second (index 1) time
    # We can't sell at the first time, since we must buy first,
    # and we can't buy and sell at the same time!
    # If we started at index 0, we'd try to buy *and* sell at time 0.
    # This would give a profit of 0, which is a problem if our
    # max_profit is supposed to be *negative*--we'd return 0.
    for current_time in xrange(1, len(stock_prices)):
        current_price = stock_prices[current_time]

        # See what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # Update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # Update min_price so it's always
        # the lowest price we've seen so far
        min_price  = min(min_price, current_price)

    return max_profit
'''