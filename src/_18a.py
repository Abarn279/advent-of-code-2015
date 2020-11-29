from file_importer import FileImporter
from aoc_utils import Vector2

def on_neighbors(grid, pos: Vector2):
    amount = 0
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            if x == 0 and y == 0: continue
            neighbor_pos = pos + Vector2(x, y)
            if neighbor_pos not in grid: continue
            if grid[neighbor_pos] == '#': amount += 1
    return amount

# Get input
inp = FileImporter.get_input("/../input/18.txt").split('\n')
grid = {}

gridsize = 100
steps = 100 # problem given

# Create grid
for y in range(gridsize):
   for x in range(gridsize):
       grid[Vector2(x, y)] = inp[y][x]

# part 2 - set corners to on
always_on = [Vector2(0, 0), Vector2(gridsize - 1, 0), Vector2(0, gridsize - 1), Vector2(gridsize - 1, gridsize - 1)]

for step in range(steps):
    newgrid = {}
    for y in range(gridsize):
        for x in range(gridsize):
            pos = Vector2(x, y)
            # intially on. stays on if 2 or 3 neighbors
            if grid[pos] == '#':
                newgrid[pos] = '#' if on_neighbors(grid, pos) in [2, 3] else '.'

            # initially off. turns on if 3 neighbors.
            else:
                newgrid[pos] = '#' if on_neighbors(grid, pos) == 3 else '.'
                
    # part 2
    for ao in always_on:
        newgrid[ao] = '#'

    grid = newgrid

print(sum(1 for i in grid.values() if i == '#'))