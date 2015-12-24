from itertools import combinations
from functools import reduce
from operator import mul


def balance(packages, groups=3):
    weight = sum(packages) // groups

    for i in range(len(packages)):
        good = [reduce(mul, x) for x in combinations(packages, i) if sum(x) == weight]
        if good:
            return min(good)


def read_instructions(file):
    with open(file) as f:
        instructions = list(map(int, f.readlines()))

    result = balance(instructions)
    print(result)

    result = balance(instructions, 4)
    print(result)


read_instructions('inputs/day_24.txt')
