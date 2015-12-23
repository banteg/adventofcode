'''
--- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?
'''

import re
from functools import partial

deer = re.compile(r'(.+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')


def parse_deer(s):
    name, *performance = deer.search(s).groups()
    speed, fly, rest = map(int, performance)
    return speed, fly, rest


def simulate(t, d):
    speed, fly, rest = d
    cycles, remain = divmod(t, fly + rest)
    total = (cycles * fly + min(fly, remain)) * speed
    return total


def read_instructions(file):
    with open(file) as f:
        deers = f.readlines()

    deers = map(parse_deer, deers)
    simulate2503 = partial(simulate, 2503)
    result = max(map(simulate2503, deers))
    print(result)


def test():
    assert simulate(1000, (14, 10, 127)) == 1120
    assert simulate(1000, (16, 11, 162)) == 1056


test()
read_instructions('inputs/day_14.txt')
