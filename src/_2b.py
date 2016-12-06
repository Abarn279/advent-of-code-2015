from file_importer import FileImporter
import itertools

# Get input
inp = [i.strip() for i in FileImporter.get_input("/../input/2.txt").split("\n")]

total = 0
for present in inp:
    x, y, z = present = sorted([int(i) for i in present.split("x")])
    wrap = 2*x + 2*y
    bow = x*y*z
    total += wrap + bow

print(total)
