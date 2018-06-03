'''
Write a function max_duffel_bag_value that takes a list of tuples
and a weight capacity, and returns the maximum monetary value the
duffel bag can hold

The tuple is stored with two indices:
    0 An integer representing the weight of the cake in kilograms
    1 An integer represeting the monetary value of the cake.


Takeaways:
    1) Make sure you spend time solving small subproblems first when you
    use DP. This is a bottom-up approach.
'''


# O(n * k) time complexity, where n is the capacity length and k is the length of the cakes tuple
# O(n) space
def find_highest_value(cakes, capacity):
    if capacity == 0:
        return -1
    max_values_at_capacity = [0] * (capacity + 1)

    for current_capacity in range(1, capacity + 1):
        max_value = 0
        for current_weight, current_value in cakes:
            if current_weight == 0 and current_value > 0:
                return float('inf')
            if current_weight <= current_capacity:
                max_value = max(max_value, current_value + max_values_at_capacity[current_capacity - current_weight])
        max_values_at_capacity[current_capacity] = max_value

    return max_values_at_capacity[-1]

cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity = 20


print('Highest value: {}'.format((find_highest_value(cake_tuples, capacity))))
