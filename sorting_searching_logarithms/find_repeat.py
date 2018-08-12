'''
We have a list of integers, where:
    1) The integers are in the range 1...n
    2) The list has a length of n + 1

The list has at least one integer which appears at least twice.
But it may have several duplicates, and each duplicate can appear more than twice.

Write a function which finds an integer that appears more than once in the list.

TAKEWAYS:
    1) For 1d arrays, always work from brute force to linear.
    2) Spot pigeonhole principle for a modified binary search.
'''

# O(n) time, O(n) space
def find_duplicate_lookup(list_with_duplicates):
    numbers = set()
    for num in list_with_duplicates:
        if num in numbers:
            return num
        else:
            numbers.add(num)

    raise Exception('No duplicates found!')

#O(n^2) time, O(1) space
def find_duplicate_brute_force(list_with_duplicates):
    for i in range(len(list_with_duplicates)):
        value = list_with_duplicates[i]
        for j in range(i + 1, len(list_with_duplicates)):
            if list_with_duplicates[i] == list_with_duplicates[j]:
                return list_with_duplicates[i]
    return 0

# O(n log n) time, O(1) space, note that this in-place sort destroys the input
def find_duplicate_sorted(list_with_duplicates):
    list_with_duplicates.sort()
    if list_with_duplicates is None or len(list_with_duplicates) <= 1:
        return 0
    prev_index = 0
    curr_index = 1
    while curr_index < len(list_with_duplicates):
        if list_with_duplicates[prev_index] == list_with_duplicates[curr_index]:
            return list_with_duplicates[prev_index]
        prev_index += 1
        curr_index += 1

    return 0

# O(n log n) time, O(1) space. This solution is stable and takes advantage of bsearch.
def find_duplicate_modified_bsearch(list_with_duplicates):
    floor = 1
    ceiling = len(list_with_duplicates) - 1

    while floor != ceiling:
        mid = floor + (ceiling - floor) // 2
        numbers_in_range = 0
        for num in list_with_duplicates:
            if floor <= num <= mid:
                numbers_in_range += 1
        if mid - floor + 1 < numbers_in_range:
            ceiling = mid
        else:
            floor = mid + 1

    return floor



a = [1, 2, 3, 4, 5, 6, 8, 8, 9, 10]
print(find_duplicate_lookup(a))
print(find_duplicate_brute_force(a))
print(find_duplicate_sorted(a))
print(find_duplicate_modified_bsearch(a))

# Solution
'''
  def find_repeat(the_list):
    floor = 1
    ceiling = len(the_list) - 1

    while floor < ceiling:
        # Divide our range 1..n into an upper range and lower range
        # (such that they don't overlap)
        # Lower range is floor..midpoint
        # Upper range is midpoint+1..ceiling
        midpoint = floor + ((ceiling - floor) / 2)
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint+1, ceiling

        # Count number of items in lower range
        items_in_lower_range = 0
        for item in the_list:
            # Is it in the lower range?
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = (
            lower_range_ceiling
            - lower_range_floor
            + 1
        )
        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            # There must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            # There must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            floor, ceiling = upper_range_floor, upper_range_ceiling

    # Floor and ceiling have converged
    # We found a number that repeats!
    return floor
'''