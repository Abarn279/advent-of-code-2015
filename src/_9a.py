from file_importer import FileImporter
from collections import deque
import sys

distances = FileImporter.get_input("/../input/9.txt").split('\n')
distance_map = {}

for d in distances:
    d = d.split(' ')
    distance_map[(d[0], d[2])] = int(d[4])
    distance_map[(d[2], d[0])] = int(d[4])

all_cities = set()
for k in distance_map.keys():
    for i in k:
        all_cities.add(i)

stack = deque()
visited = set()

for ac in all_cities:
    stack.appendleft(((ac,), 0)) # tuple of cities visited, current distance

c_best = sys.maxsize

while len(stack) > 0:
    [cities, dist] = stack.popleft()

    # pruning for if we can't possibly get another best
    if dist >= c_best:
        continue

    current_city_set = set(cities) 

    if current_city_set == all_cities:
        c_best = dist
        continue

    # get set of remaining cities to go to 
    remaining_city_set = all_cities - current_city_set

    for remaining in remaining_city_set:
        new_path = cities + (remaining,)
        new_dist = dist + distance_map[(cities[-1], remaining)]
        stack.appendleft((new_path, new_dist))

print(c_best)
