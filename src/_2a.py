from file_importer import FileImporter
import itertools

# Get input
inp = [i.strip() for i in FileImporter.get_input("/../input/2.txt").split("\n")]

total = 0
for present in inp:
    present = [int(i) for i in present.split("x")]
    combinations = list(itertools.combinations(present, 2))
    needed_paper = sum([2 * (i[0] * i[1]) for i in combinations]) + min([i[0] * i[1] for i in combinations])
    total += needed_paper
print(total)
