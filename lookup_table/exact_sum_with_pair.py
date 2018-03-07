'''
Write a function that takes flight_length, and a list
of integers and returns a boolean indicating whether
there are two that numbers in list that sum to flight_length


Takeaways:
    1) Use hash tables for O(1) lookup and insert
'''

# O(n) time, O(n) space
def can_two_movies_fill_flight(movie_lengths, flight_length):
    movie_times = set()
    for movie_length in movie_lengths:
        if flight_length - movie_length in movie_times:
            return True
        movie_times.add(movie_length)
    return False


flight_length = 10
negative_movie_lengths = [9, 3, 10, 4, 2]
movie_lengths = [9, 3, 10, 4, 11, 1]
single_movie_lengths = [1, 5]
print(can_two_movies_fill_flight(negative_movie_lengths, flight_length))
print(can_two_movies_fill_flight(movie_lengths, flight_length))
print(can_two_movies_fill_flight(single_movie_lengths, flight_length))
