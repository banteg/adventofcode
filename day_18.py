from copy import deepcopy
from itertools import chain

rows = 100
cols = 100


def load_state(txt):
    state = []
    for line in txt:
        state.append([])
        for char in line.strip():
            if char == '#':
                state[-1].append(1)
            elif char == '.':
                state[-1].append(0)
            else:
                raise Exception('unknown char')

    return state


def apply_rules(state):
    shadow = deepcopy(state)
    for row in range(rows):
        for col in range(cols):
            neighbours = sum(get_neighbours(shadow, row, col))
            if shadow[row][col] == 0 and neighbours == 3:
                state[row][col] = 1
            if shadow[row][col] and (neighbours < 2 or neighbours > 3):
                state[row][col] = 0

    return state


def get_neighbours(shadow, row, col):
    neighbours = []
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == dy == 0:
                continue
            if 0 <= row + dx < rows and 0 <= col + dy < cols:
                neighbours.append(shadow[row + dx][col + dy])

    return neighbours


def illuminate(state, steps, stuck=False):
    for i in range(steps):
        if stuck:
            state[0][0] = state[0][99] = state[99][0] = state[99][99] = 1
        state = apply_rules(state)

    if stuck:
        state[0][0] = state[0][99] = state[99][0] = state[99][99] = 1
    return state


def read_instructions(file):
    with open(file) as f:
        lines = f.readlines()

    state = load_state(lines)
    state = illuminate(state, 100)
    on = sum(chain.from_iterable(state))
    print(on)

    state = load_state(lines)
    state = illuminate(state, 100, stuck=True)
    on = sum(chain.from_iterable(state))
    print(on)


read_instructions('inputs/day_18.txt')
