'''
Write a class TempTracker with the following methods:
    1) insert() - records a new temperature
    2) get_max() - records the highest temp we've seen so far
    3) get_min() - returns the lowest temp we've seen so far
    4) get_mean() - returns the mean of all temps we've seen so far (float)
    5) get_mode() - returns a mode of all temps we've seen so far
        (if there is more than one mode, return any of the nodes)

Temperatures will all be inserted as integers. We can assume they will be in range [0...110]


Takeaways:
    1) Treat OOP design problems like they are system design questions
    2) Know tradeoffs between ahead-of-time and just-in-time
'''

class TempTracker(object):
    def __init__(self):
        self.max = 0
        self.min = float('inf')
        self.mean = None
        self.mode = None
        self.__total = 0
        self.__number_of_readings = 0
        self.__temperature_counts = [0] * 111
        self.__max_count = 0

    def insert_reading(self, reading):
        self.max = max(self.max, reading)
        self.min = min(self.min, reading)

        self.__number_of_readings += 1
        self.__total += reading
        self.mean = self.__total / self.__number_of_readings

        self.__temperature_counts[reading] += 1
        if self.__temperature_counts[reading] > self.__max_count:
            self.mode = reading
            self.__max_count = self.__temperature_counts[reading]

    def get_max(self):
        if self.max is None:
            raise Exception('Null max value')
        return self.max

    def get_min(self):
        if self.min is None:
            raise Exception('Null min value')
        return self.min

    def get_mean(self):
        if self.mean is None:
            raise Exception('Null mean value')
        return self.mean

    def get_mode(self):
        if self.mode is None:
            raise Exception('Null mode value')
        return self.mode


tracker = TempTracker()
tracker.insert_reading(10)
tracker.insert_reading(20)
tracker.insert_reading(10)
tracker.insert_reading(20)
tracker.insert_reading(20)

print('Min: {}'.format(tracker.min))
print('Max: {}'.format(tracker.max))
print('Mean: {}'.format(tracker.mean))
print('Mode: {}'.format(tracker.mode))
