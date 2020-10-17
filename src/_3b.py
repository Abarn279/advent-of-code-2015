from file_importer import FileImporter
from aoc_utils import Vector2
from collections import defaultdict

DIRECTIONS = {'^': Vector2(0, 1), '>': Vector2(1, 0), 'v': Vector2(0, -1), '<': Vector2(-1, 0)}

# Get input
inp = FileImporter.get_input("/../input/3.txt")

houses = defaultdict(lambda: 0)
pos = Vector2(0, 0)
robo_pos = Vector2(0, 0)
houses[pos] += 1

for ind, direc in enumerate(inp):
    if ind % 2 == 0: #santa
        pos = pos + DIRECTIONS[direc]
        houses[pos] += 1
    else: #robo
        robo_pos = robo_pos + DIRECTIONS[direc]
        houses[robo_pos] += 1

print(sum(1 for i in houses.values() if i > 0))