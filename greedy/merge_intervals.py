'''
Write a function merge_ranges() that takes a list of meeting time
ranges and returns a list of condensed ranges

Takeaways:
    1) Work to identify edge cases.
    2) Consider using a sort, especially if you need a greedy algorithm
'''
# O(n^2) time best case, O(n) space worst case
def merge_ranges_bf(meeting_time_ranges):
    merged_meetings = []
    i = 0
    while i < len(meeting_time_ranges):
        start_time = meeting_time_ranges[i][0]
        end_time = meeting_time_ranges[i][1]
        j = 0
        while j < len(meeting_time_ranges):
            if i != j:
                other_start = meeting_time_ranges[j][0]
                other_end = meeting_time_ranges[j][1]
                if start_time <= other_start <= end_time or start_time <= other_end <= end_time:
                    start_time = min(start_time, other_start)
                    end_time = max(end_time, other_end)
                    meeting_time_ranges.remove((other_start, other_end))
                    j -= 1
            j += 1
        merged_meetings.append((start_time, end_time))
        i += 1
    return merged_meetings

happy = [(0,1), (3,5), (4,8), (10, 12), (9,10)]
all_merge = [(1,10), (2,6), (3, 5), (7, 9)]
touch = [(1,2), (3, 4)]
subsume = [(1,5), (2,3)]
print('Brute force solution')
print(merge_ranges_bf(happy))
print(merge_ranges_bf(all_merge))
print(merge_ranges_bf(touch))
print(merge_ranges_bf(subsume))

# O(n log n) solution, O(n) space
def merge_ranges(meetings):
    meetings = sorted(meetings)
    merged_meetings = [meetings[0]]
    for start_time, end_time in meetings[1:]:
        last_merged_start, last_merged_end = merged_meetings[-1]
        if start_time <= last_merged_end:
            merged_meetings[-1] = (last_merged_start, max(end_time, last_merged_end))
        else:
            merged_meetings.append((start_time, end_time))
    return merged_meetings

happy = [(0,1), (3,5), (4,8), (10, 12), (9,10)]
all_merge = [(1,10), (2,6), (3, 5), (7, 9)]
touch = [(1,2), (3, 4)]
subsume = [(1,5), (2,3)]
print('Sorted solution')
print(merge_ranges(happy))
print(merge_ranges(all_merge))
print(merge_ranges(touch))
print(merge_ranges(subsume))
