from file_importer import FileImporter
from collections import defaultdict
import re
from aoc_utils import Vector2

def do_grid(grid, start_pos: Vector2, end_pos: Vector2, operator):
    for x in range(start_pos.x, end_pos.x + 1):
        for y in range(start_pos.y, end_pos.y + 1):
            if operator == 0: #on
                grid[Vector2(x, y)] += 1
            elif operator == 1: #off
                grid[Vector2(x, y)] = max(0, grid[Vector2(x, y)] - 1)
            elif operator == 2: #toggle
                grid[Vector2(x, y)] += 2

# Get input
inp = FileImporter.get_input("/../input/6.txt").split('\n')
grid = defaultdict(lambda: 0)

for i in inp:
    start, end = map(lambda x: x.split(','), re.match("[\w\s]+ (\d+,\d+) \w+ (\d+,\d+)", i).groups())
    start = Vector2(int(start[0]), int(start[1])); end = Vector2(int (end[0]), int(end[1]))

    if 'turn on' in i:
        operator = 0
    elif 'turn off' in i:
        operator = 1
    elif 'toggle' in i:
        operator = 2

    do_grid(grid, start, end, operator)

print(sum(i for i in grid.values()))