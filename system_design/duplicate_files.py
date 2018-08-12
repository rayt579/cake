'''
Write a function that returns a list of all the duplicate files.

To help us confirm that two files are actually duplicates, return a list of tuples where:
    the first item is the duplicate file
    the second item is the original file

You can assume each file was only duplicated once


TAKEAWAYS:
    1) Be prepared for ambiguous questions.
    2) Be able to discuss key assumptions.
    3) Look for incremental improvements (early breaks).
'''

import os

# Interview Cake Breakdown Solution
# Time cost: O(b), where b is the size of all files from the starting directory
# Space cost: O(b), where b is the size of all files from the starting directory
def find_duplicate_files_inefficient(starting_directory):
    files_seen_already = {}
    stack = [starting_directory]

    #we'll track tuples of (duplicate_file, original_file)
    duplicates = []
    while len(stack) > 0:
        current_path = stack.pop()

        #if it's a directory put the contents in our stack
        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                full_path = os.path.join(current_path, path)
                stack.append(full_path)

        #if it's a file
        else:
            with open(current_path) as file:
                file_contents = file.read()
            current_last_edited_time = os.path.getmtime(current_path)

            # if we've seen it before
            if file_contents in files_seen_already:
                existing_last_edited_time, existing_path = files_seen_already[file_contents]

                if current_last_edited_time > existing_last_edited_time:
                    #current file is the dupe!
                    duplicates.append((current_path, existing_path)
                else:
                    #old file is the dupe!
                    #so delete it
                    duplicates.append((existing_path, current_path))
                    files_seen_already[file_contents] = (current_last_edited_time, current_path)

            # if it's a new file, throw it in files_seen_already
            # and record the path and the last edited time, so we can delete later if it's a dupe
            else:
                files_seen_already[file_contents] = (current_last_edited_time, current_path)

    return duplicates


import hashlib

# O(n) time, O(n) space. This is where n is the number of files for the filesystem target.
def find_duplicate_files_linear(starting_directory):
    files_seen_already = {}
    stack = [starting_directory]

    #we'll track tuples of (duplicate_file, original_file)
    duplicates = []
    while len(stack) > 0:
        current_path = stack.pop()

        #if it's a directory put the contents in our stack
        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                full_path = os.path.join(current_path, path)
                stack.append(full_path)

        #if it's a file
        else:
            file_contents = sample_hash_file(current_path)
            current_last_edited_time = os.path.getmtime(current_path)

            # if we've seen it before
            if file_contents in files_seen_already:
                existing_last_edited_time, existing_path = files_seen_already[file_contents]

                if current_last_edited_time > existing_last_edited_time:
                    #current file is the dupe!
                    duplicates.append((current_path, existing_path)
                else:
                    #old file is the dupe!
                    #so delete it
                    duplicates.append((existing_path, current_path))
                    files_seen_already[file_contents] = (current_last_edited_time, current_path)

            # if it's a new file, throw it in files_seen_already
            # and record the path and the last edited time, so we can delete later if it's a dupe
            else:
                files_seen_already[file_contents] = (current_last_edited_time, current_path)

    return duplicates

# Helper function that opens the file, returns hash from first, second, third contents of the file,
# Hashes in constant time O(4000 * 3)
def sample_hash_file(path):
    num_bytes_to_read_per_sample = 4000
    total_bytes = os.path.getsize(path)
    hasher = hashlib.sha512()

    with open(path, 'rb') as file:

        # if the file is too short to take 3 samples, hash the entire file
        if total_bytes < num_bytes_to_read_per_sample * 3:
            hasher.update(file.read())

        else:
            num_bytes_between_samples = (total_bytes - num_bytes_to_read_per_sample * 3) / 2
            for offset_multiplier in range(3):
                start_of_sample = offset_multiplier * (num_bytes_to_read_per_sample + num_bytes_between_samples)
                file.seek(start_of_sample)
                sample = file.read(num_bytes_to_read_per_sample)
                hasher.update(sample)

    return hasher.hexdigest()
