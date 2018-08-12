'''
Given a rotated sorted list, write a function
to return the rotation point
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

'''
  def find_rotation_point(words):
    first_word = words[0]
    floor_index = 0
    ceiling_index = len(words) - 1

    while floor_index < ceiling_index:
        # Guess a point halfway between floor and ceiling
        guess_index = floor_index + ((ceiling_index - floor_index) / 2)

        # If guess comes after first word or is the first word
        if words[guess_index] >= first_word:
            # Go right
            floor_index = guess_index
        else:
            # Go left
            ceiling_index = guess_index

        # If floor and ceiling have converged
        if floor_index + 1 == ceiling_index:
            # Between floor and ceiling is where we flipped to the beginning
            # so ceiling is alphabetically first
            return ceiling_index
'''