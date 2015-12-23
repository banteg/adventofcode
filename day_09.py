'''
--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?
'''

import re
from itertools import permutations

distance = re.compile(r'(.*) to (.*) = (\d+)')


def parse_distance(s):
    a, b, d = distance.search(s).groups()
    d = int(d)
    return tuple(sorted([a, b])), d


def travel(s):
    distances = {}
    locations = set()
    for loc, dist in map(parse_distance, s.split('\n')):
        distances[loc] = dist
        locations.update(loc)

    best = float('inf')
    for path in permutations(locations):
        dist = 0
        for a, b in zip(path, path[1:]):
            dist += distances[tuple(sorted([a, b]))]
        if dist < best:
            best = dist

    print(best)
    return best


def read_instructions(file):
    with open(file) as f:
        instructions = f.read().strip()
    travel(instructions)


def test():
    travel('London to Dublin = 464\nLondon to Belfast = 518\nDublin to Belfast = 141')

test()
read_instructions('inputs/day_09.txt')
