import re
from collections import defaultdict


def calibrate(molecule, replacements):
    for atom, isotopes in replacements.items():
        for r in re.finditer(atom, molecule):
            a, b = r.span(0)
            for isotope in isotopes:
                yield molecule[:a] + isotope + molecule[b:]


def read_instructions(file):
    with open(file) as f:
        data = f.readlines()

    molecule = data[-1].strip()

    replacements = defaultdict(list)
    for repl in data[:-2]:
        a, b = repl.split(' => ')
        replacements[a].append(b.strip())

    result = set(calibrate(molecule, replacements))
    print(len(result))


read_instructions('inputs/day_19.txt')


def fabricate():
    with open('inputs/day_19.txt') as f:
        data = f.readlines()

    molecule = data[-1].strip()
    repl = []
    for x in data[:-2]:
        a, b = x.split(' => ')
        repl.append((b.strip(), a))

    steps = 0
    target = molecule
    while target != 'e':
        for a, b in repl:
            if a not in target:
                continue
            target = target.replace(a, b, 1)
            steps += 1
    return steps

print(fabricate())
