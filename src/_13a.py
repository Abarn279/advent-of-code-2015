from file_importer import FileImporter
from collections import deque
import sys

happinesses = FileImporter.get_input("/../input/13.txt").split('\n')
happiness_map = {}

for h in happinesses:
    h = h.replace('.', '').split(' ')
    val = int(h[3]) if h[2] == 'gain' else -int(h[3])
    happiness_map[(h[0], h[10])] = val

all_people = set()
for k in happiness_map.keys():
    for i in k:
        all_people.add(i) 

# add self for part 2
for p in all_people:
    happiness_map[('Me', p)] = 0
    happiness_map[(p, 'Me')] = 0
all_people.add('Me')

stack = deque()
visited = set()

for ap in all_people:
    stack.appendleft(((ap,), 0)) # tuple of cities visited, current happiness

c_best = -1

while len(stack) > 0:
    [c_people, c_happiness] = stack.popleft()

    current_people_set = set(c_people) 

    if current_people_set == all_people:
        added_happiness = happiness_map[(c_people[-1], c_people[0])] + happiness_map[(c_people[0], c_people[-1])] # need to complete the circle of happiness
        if c_happiness + added_happiness > c_best:
            c_best = c_happiness + added_happiness
            continue

    # get set of remaining cities to go to 
    remaining_people_set = all_people - current_people_set

    for remaining in remaining_people_set:
        new_people = c_people + (remaining,)
        new_happiness_change = c_happiness + happiness_map[(c_people[-1], remaining)] + happiness_map[(remaining, c_people[-1])]
        stack.appendleft((new_people, new_happiness_change))

print(c_best)
