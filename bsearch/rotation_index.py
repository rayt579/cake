'''
Given a rotated sorted list, write a function
to return the rotation point

Takeaways:
    1) Searching for an index is a no brainer binary search
    2) Make sure you watch for off by one errors
'''
# O(log n) time, O(1) space
def find_rotation(words):
    lo, hi = 0, len(words) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if 0 < mid < len(words) - 1 and  words[mid] < words[mid - 1] and words[mid] < words[mid + 1]:
            return mid
        elif mid == len(words) - 1 and words[0] > words[mid]:
            return mid
        elif words[mid] < words[0]:
            hi = mid - 1
        else:
            lo = mid + 1
        print('lo: {}, mid:{}, hi:{}'.format(lo, mid, hi))
    return 0


happy = ['f', 'g', 'a', 'c']
beginning = ['a', 'b', 'c']
end = ['b', 'c', 'a']
print(find_rotation(happy))
print(find_rotation(beginning))
print(find_rotation(end))
