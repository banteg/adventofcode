import re

rev = {}
register = {}


def parse(wire, offset=0):
    if wire in register:
        return register[wire]

    if wire not in rev:
        return int(wire)

    i = rev[wire]
    print(' ' * offset, wire, i)

    if len(i) == 1:
        if re.match(r'[a-z]+', i[0]):
            return parse(i[0], offset+1)
        else:
            return int(i[0])
    elif i[0] == 'NOT':
        a = parse(i[1], offset+1)
        register[wire] = ~ a & 0xffff
    elif i[1] == 'OR':
        a = parse(i[0], offset+1)
        b = parse(i[2], offset+1)
        register[wire] = a | b & 0xffff
    elif i[1] == 'AND':
        a = parse(i[0], offset+1)
        b = parse(i[2], offset+1)
        register[wire] = a & b & 0xffff
    elif i[1] == 'LSHIFT':
        a = parse(i[0], offset+1)
        b = parse(i[2], offset+1)
        register[wire] = a << b & 0xffff
        return register[wire]
    elif i[1] == 'RSHIFT':
        a = parse(i[0], offset+1)
        b = parse(i[2], offset+1)
        register[wire] = a >> b & 0xffff

    return register[wire]


def read_instructions(file):
    with open(file) as f:
        instructions = f.readlines()

    for i in instructions:
        left, right = i.split(' -> ')
        left = left.split()
        rev[right.strip()] = left

    print(parse('a'))


read_instructions('inputs/day_07.txt')
