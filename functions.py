import math
import random

from cars import Car


def closest_point(car, points):
    min_dist = 200
    min_x = -1
    min_y = -1
    for row in points:
        dist = math.sqrt((row[0]-car.position[0])**2+(row[1]-car.position[1])**2)
        if dist < min_dist:
            czy_odbior = (row[3] == 'Deliver')
            if czy_odbior:
                zaladunek_po_odbiorze = row[2] + car.actual_load
            else:
                zaladunek_po_odbiorze = car.actual_load - row[2]
            if czy_odbior and zaladunek_po_odbiorze <= car.capacity:
                min_dist = dist
                min_x = row[0]
                min_y = row[1]
            elif not czy_odbior and zaladunek_po_odbiorze > 0:
                min_dist = dist
                min_x = row[0]
                min_y = row[1]
    if min_dist < 200:
        car.position = [min_x, min_y]
    return [min_x, min_y, min_dist]


def closest_magazine(car, points):
    min_dist = 200
    min_x = -1
    min_y = -1
    for row in points:
        dist = math.sqrt((row[0] - car.position[0]) ** 2 + (row[1] - car.position[1]) ** 2)
        if dist < min_dist:
            min_dist = dist
            min_x = row[0]
            min_y = row[1]
    car.position = [min_x, min_y]
    return [min_x, min_y, min_dist]

def time(car, distance):
    return round(distance/car.speed, 2)


def check_break(car):
    if car.time_to_break >= 180:
       car.time += 10
       car.time_to_break = 0

def generate_map():
    map = []
    for i in range(10000):
        b = int(i / 100)
        c = i % 100
        map.append([b, c, ""])

    n = random.randint(405, 605)
    points = random.sample(range(10000), n)
    for i in range(n - 5):
        a = points[i]
        map[a][2] = "delivery"

    for i in range(5):
        a = points[n - 5 + i]
        map[a][2] = "magazine"
    return map


def generate_magazine_coordinates(map):
    magazine = []
    result = [i for i, x in enumerate(map) if x[2] == "magazine"]
    for i in range(5):
        magazine.append([map[int(result[i])][0], map[int(result[i])][1]])
    return magazine


def generate_delivery_coordinates(map):
    result = [i for i, x in enumerate(map) if x[2] == "delivery"]
    delivery = []
    for i in range(len(result)):
        delivery.append([map[int(result[i])][0], map[int(result[i])][1],
                         random.randint(100, 200), random.choice(["deliver", "pickup"])])
    return delivery

