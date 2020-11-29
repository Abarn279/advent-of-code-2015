import itertools
import math

containers = '''50
44
11
49
42
46
18
32
26
40
21
7
18
43
10
47
36
24
22
40''' # input

liters = 150 # problem given

containers = list(map(int, containers.split('\n')))
total = 0
found = False
for c_length in range(1, math.ceil(len(containers) / 2) + 1): # this is a guess to how big a combo can be. not likely that you use over half and then still are under the liter count.
    for combo in itertools.combinations(containers, c_length):
        if sum(combo) == liters:
            total += 1
            found = True
    if found: break

print(total)