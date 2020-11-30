reg = {'a':1, 'b':0}

prog = '''jio a, +19
inc a
tpl a
inc a
tpl a
inc a
tpl a
tpl a
inc a
inc a
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
jmp +23
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
inc a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7
'''.split('\n')

i = 0
while i < len(prog):
    line = prog[i]
    inst = line[:3]

    if inst == 'hlf':
        r = prog[i].split(' ')[1]
        reg[r] = reg[r] / 2

    elif inst == 'tpl':
        r = prog[i].split(' ')[1]
        reg[r] = reg[r] * 3

    elif inst == 'inc':
        r = prog[i].split(' ')[1]
        reg[r] = reg[r] + 1

    elif inst == 'jmp':
        o = prog[i].split(' ')[1]
        i = i + int(o)
        continue

    elif inst == 'jie':
        pass
        [inst, r, o] = prog[i].split(' ')
        r = r[:-1]
        if reg[r] % 2 == 0:
            i = i + int(o)
            continue

    elif inst == 'jio':
        [inst, r, o] = prog[i].split(' ')
        r = r[:-1]
        if reg[r] == 1:
            i = i + int(o)
            continue

    i += 1

print(reg)