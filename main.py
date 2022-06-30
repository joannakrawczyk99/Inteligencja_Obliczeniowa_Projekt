from functions import generate_map, generate_magazine_coordinates, generate_delivery_coordinates
from cars import shuffle_cars
from functions import closest_point, closest_magazine, time, check_break
import plotly.express as px
import pandas as pd
import random


map = generate_map()
magazine = generate_magazine_coordinates(map)
delivery = generate_delivery_coordinates(map)
cars = shuffle_cars(magazine)

print(f'Magazines: {magazine}')
print(f'Delivery: {delivery}')

print(*cars, sep='\n')

magazines_coords = pd.DataFrame(magazine, columns=['x', 'y'])
delivery_points = pd.DataFrame(delivery, columns=['x', 'y', 'size', 'deliver/pickup'])
print(delivery_points)


fig = px.scatter(delivery_points, x='x', y='y', color=delivery_points['deliver/pickup'])
fig.add_scatter(x=magazines_coords['x'], y=magazines_coords['y'], mode="markers", name='magazine')
fig.show()


routes = []
for i in cars:
    routes.append({'x': [i.position[0]], 'y': [i.position[1]]})

uni = (random.choice(delivery))
while True:
    for i, k in enumerate(cars):
        p = closest_point(k, delivery)
        delivered = [j for j, x in enumerate(delivery) if x[0] == p[0] and x[1] == p[1]]

        if len(delivered) > 0:

            if delivery[delivered[0]][3] == 'pickup':
                k.actual_load = k.actual_load + delivery[delivered[0]][2]

            else:
                k.actual_load = k.actual_load - delivery[delivered[0]][2]

            k.time_to_break += time(k, p[2])
            k.time += time(k, p[2]) + (k.loading * delivery[delivered[0]][2])
            k.distance += p[2]

            check_break(k)

            if delivery[delivered[0]] == uni:
                k.time += 720

            delivery.pop(delivered[0])

        else:
            p = closest_magazine(k, magazine)
            k.actual_load = k.capacity * 0.8

        routes[i]['x'].append(p[0])
        routes[i]['y'].append(p[1])
        if len(delivery) == 0:
            break
    if len(delivery) == 0:
        break

tab = []
for i in range(len(cars)):
    df = pd.DataFrame(data=routes[i])
    tab.append(df)
for i, t in enumerate(tab):
    fig.add_scatter(x=t['x'], y=t['y'], name=f'car_{i+1}')

fig.show()

final_time = []
final_distance = []
for s in cars:
    final_time.append(round(s.time/60,2))
    final_distance.append(round(s.distance,2))

print("All points on the map: ", (len(delivery) + len(magazine)))
print("All cars: ", len(cars))
print("Car travel times: ", final_time)
print("Distance traveled: ", final_distance)

