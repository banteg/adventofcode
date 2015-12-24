import re


def maybe_int(x):
    try:
        return int(x)
    except ValueError:
        return x


def parse(i):
    parts = re.split(r' |, ', i.strip())
    if len(parts) == 2:
        parts.append('')
    return list(map(maybe_int, parts))


def turing(cmds, a=0, b=0):
    registers = {'a': a, 'b': b}
    i = 0
    while 0 <= i < len(cmds):
        c, r, j = parse(cmds[i])
        if c == 'hlf':
            registers[r] = registers[r] // 2
            i += 1
        if c == 'tpl':
            registers[r] = registers[r] * 3
            i += 1
        if c == 'inc':
            registers[r] += 1
            i += 1
        if c == 'jmp':
            i += r
        if c == 'jie':
            if not registers[r] % 2:
                i += j
            else:
                i += 1
        if c == 'jio':
            if registers[r] == 1:
                i += j
            else:
                i += 1

        # print(i, c, r, j, registers)

    return registers


def read_instructions(file):
    with open(file) as f:
        instructions = f.readlines()

    one = turing(instructions)
    two = turing(instructions, a=1)
    print(one['b'], two['b'], sep='\n')


read_instructions('inputs/day_23.txt')
