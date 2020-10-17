from file_importer import FileImporter
from aoc_utils import Vector2
from collections import defaultdict

DIRECTIONS = {'^': Vector2(0, 1), '>': Vector2(1, 0), 'v': Vector2(0, -1), '<': Vector2(-1, 0)}

# Get input
inp = FileImporter.get_input("/../input/3.txt")

houses = defaultdict(lambda: 0)
pos = Vector2(0, 0)
houses[pos] += 1

for i in inp:
    pos = pos + DIRECTIONS[i]
    houses[pos] += 1

print(sum(1 for i in houses.values() if i > 0))