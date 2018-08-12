'''
Write a function that takes flight_length, and a list
of integers and returns a boolean indicating whether
there are two that numbers in list that sum to flight_length


Takeaways:
    1) Use hash tables for O(1) lookup and insert
    2) Consider using binary search to save space.

Bonus:
	1) What if we wanted the movie lengths to sum to something close to the flight length (say, within 20 minutes)?
	2) What if we wanted to fill the flight length as nicely as possible with any number of movies (not just 2)?
	3) What if we knew that movie_lengths was sorted? Could we save some space and/or time?
'''

# O(n) time, O(n) space
def can_two_movies_fill_flight(movie_lengths, flight_length):
    movie_times = {}
    for movie_length in movie_lengths:
        if flight_length - movie_length in movie_times:
            return True
        movie_times[movie_length] = 1
    return False


flight_length = 10
negative_movie_lengths = [9, 3, 10, 4, 2]
movie_lengths = [9, 3, 10, 4, 11, 1]
single_movie_lengths = [1, 5]
print(can_two_movies_fill_flight(negative_movie_lengths, flight_length))
print(can_two_movies_fill_flight(movie_lengths, flight_length))
print(can_two_movies_fill_flight(single_movie_lengths, flight_length))



#Solution'
'''
def can_two_movies_fill_flight(movie_lengths, flight_length):
    # Movie lengths we've seen so far
    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        matching_second_movie_length = flight_length - first_movie_length
        if matching_second_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)

    # We never found a match, so return False
    return False
'''