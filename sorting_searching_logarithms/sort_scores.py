'''
Write a function that takes a list of unsorted scores,
and the highest possible score in the game and returns a
sorted list of scores in less than O(n log n) time

Takeaways:
    1) Consider out-of-place sort by creating new input
    2) Consider how to generate answers
    3) You can use a list as a lookup table

Bonus:
1) Note that by optimizing for time we ended up incurring some space cost! What if we were optimizing for space?
2) We chose to generate and return a separate, sorted list. Could we instead sort the list in place? Does this change the time complexity? The space complexity?
'''

# O(n + m) time, where n is len(unsorted_scores) and m is the highest_possible_score
def sort_scores(unsorted_scores, highest_possible_score):
    score_counts = [0] * (highest_possible_score + 1)
    sorted_scores = []
    for score in unsorted_scores:
        score_counts[score] += 1
    for i in range(highest_possible_score, -1, -1):
        while score_counts[i] > 0:
            sorted_scores.append(i)
            score_counts[i] -= 1
    return sorted_scores


unsorted = [37, 89, 41, 65, 91, 53]
hpc = 100

print(sort_scores(unsorted, hpc))
# Solution
'''
  def counting_sort(the_list, max_value):
    # List of 0's at indices 0...max_value
    num_counts = [0] * (max_value + 1)

    # Populate num_counts
    for item in the_list:
        num_counts[item] += 1

    # Populate the final sorted list
    sorted_list = []

    # For each item in num_counts
    for item, count in enumerate(num_counts):

        # For the number of times the item occurs
        for _ in xrange(count):

            # Add it to the sorted list
            sorted_list.append(item)

    return sorted_list
'''