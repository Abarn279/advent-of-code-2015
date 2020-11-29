from file_importer import FileImporter
from re import match

inp = FileImporter.get_input("/../input/16.txt").split('\n')

tape = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

final = None
for i in inp:
    [suenum, thing1, amount1, thing2, amount2, thing3, amount3] = match('Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)', i).groups()

    valid = True
    things = [thing1, thing2, thing3]
    amounts = list(map(int, [amount1, amount2, amount3]))

    for thing_i in [0, 1, 2]:
        if things[thing_i] in ['cats', 'trees']:
            if amounts[thing_i] <= tape[things[thing_i]]:
                valid = False
                break
        elif things[thing_i] in ['pomeranians', 'goldfish']:
            if amounts[thing_i] >= tape[things[thing_i]]:
                valid = False
                break
        else:
            if amounts[thing_i] > tape[things[thing_i]] or (amounts[thing_i] == 0 and things[thing_i] not in ['akitas', 'vizslas']):
                valid = False
                break
    
    if valid == True:
        final = suenum
        break


print(final)