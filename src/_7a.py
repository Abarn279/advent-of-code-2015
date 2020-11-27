from file_importer import FileImporter
from collections import deque

# Get input
instructions = FileImporter.get_input("/../input/7.txt").split('\n')
instructions = sorted(instructions, key = lambda x: len(x))
instructions = deque(instructions)
wires = {}

gv = lambda v: int(v) if v.isdigit() else wires[v]

def wset(s,x): 
        wires[x] = s
def wand(x,y,z): 
    wires[z] = x & y
def wor(x,y,z): 
    wires[z] = x | y
def wlshift(p,a,q): 
    wires[q] = p << a
def wrshift(p,a,q): 
    wires[q] = p >> a
def wnot(e,f): 
    wires[f] = (~e + 2**16)

while len(instructions) > 0:
    inst = instructions.popleft()
    print(len(instructions))
    i = inst.split(' ')

    # make sure input wires have been set for and/or
    if i[1] in ['AND', 'OR']:
        if (not i[0].isdigit() and i[0] not in wires) or (not i[2].isdigit() and i[2] not in wires):
            instructions.append(inst)
            continue
    
    # make sure input wires have been set for shifts
    elif i[1] in ['RSHIFT', 'LSHIFT']:
        if not i[0].isdigit() and i[0] not in wires:
            instructions.append(inst)
            continue

    # make sure input wires have been set for NOT
    elif i[0] == 'NOT':
        if not i[1].isdigit() and i[1] not in wires:
            instructions.append(inst)
            continue

    else:
        if not i[0].isdigit():
            if i[0] not in wires:
                instructions.append(inst)
                continue

    if i[1] == 'AND':
        wand(gv(i[0]), gv(i[2]), i[4])
    elif i[1] == 'OR':
        wor(gv(i[0]), gv(i[2]), i[4])
    elif i[1] == 'LSHIFT':
        wlshift(gv(i[0]), int(i[2]), i[4])
    elif i[1] == 'RSHIFT':
        wrshift(gv(i[0]), int(i[2]), i[4])
    elif i[0] == 'NOT':
        wnot(gv(i[1]), i[3])
    else:
        wset(gv(i[0]), i[2])

print(wires['a'])