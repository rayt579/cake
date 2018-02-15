'''
Write a function that takes a list of unsorted scores,
and the highest possible score in the game and returns a
sorted list of scores in less than O(n log n) time

Takeaways:
    1) Consider out-of-place sort by creating new input
    2) Consider how to generate answers
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
