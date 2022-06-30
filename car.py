class Car:

    def __init__(self, loading, position, capacity, speed, actual_load, course_done, color):
        self.unloading = 0.033
        self.loading = loading
        self.position = position
        self.capacity = capacity
        self.speed = speed
        self.actual_load = actual_load
        self.course_done = course_done
        self.color = color
        self.time = 0
        self.time_to_break = 0
        self.distance = 0


    def __str__(self):
        return f'Color: {self.color}, '\
               f'Capacity: {self.capacity}, '\
               f'Speed: {self.speed}, ' \
               f'Loading: {self.loading}, ' \
               f'Unloading: {self.unloading}, '\
               f'Actual loading: {self.actual_load}, '\
               f'Position: {self.position}, ' \
               f'Execution: {self.course_done}'






