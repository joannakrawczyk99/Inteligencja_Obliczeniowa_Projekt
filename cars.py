from car import Car
import random


def shuffle_cars(magazine):
    coutner = random.randint(3, 6)
    cars = []

    for i in range(coutner):
        course_done = False
        color = random.choice(["Green", "Blue", "Red"])
        position = random.choice(magazine)

        loading = 0
        speed = 1.5
        capacity = 1000
        actual_load = 0

        if color == "Green":
            loading = 0.016
            speed = 1.5
            capacity = 1000
            actual_load = capacity/2

        elif color == "Blue":
            loading = 0.033
            speed = 1
            capacity = 1500
            actual_load = capacity/2

        elif color == "Red":
            loading = 0.05
            speed = 0.75
            capacity = 2000
            actual_load = capacity/2

        s = Car(loading, position, capacity, speed, actual_load, course_done, color)

        cars.append(s)
    return cars
