'''
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?

--- Part Two ---

You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.
'''

import re
from itertools import chain


parser = re.compile(r'(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)')


def switch_lights(instructions, ancient=False):
    if ancient:
        lights = [[0] * 1000 for _ in range(1000)]
        commands = {
            'turn on': lambda x: x + 1,
            'turn off': lambda x: max(x - 1, 0),
            'toggle': lambda x: x + 2,
        }
    else:
        lights = [[False] * 1000 for _ in range(1000)]
        commands = {
            'turn on': lambda x: True,
            'turn off': lambda x: False,
            'toggle': lambda x: not x,
        }

    for i in instructions:
        command, *coords = parser.search(i).groups()
        ax, ay, bx, by = tuple(map(int, coords))
        for x in range(ax, bx + 1):
            for y in range(ay, by + 1):
                lights[x][y] = commands[command](lights[x][y])

    lit = sum(chain.from_iterable(lights))
    return lit


def test():
    assert switch_lights(['turn on 0,0 through 999,999']) == 1000000
    assert switch_lights(['toggle 0,0 through 999,0']) == 1000
    assert switch_lights(['turn off 499,499 through 500,500']) == 0


def read_instructions(file):
    with open(file) as f:
        instructions = f.readlines()

    lit = switch_lights(instructions)
    print(lit)

    lit_ancient = switch_lights(instructions, ancient=True)
    print(lit_ancient)


test()
read_instructions('inputs/day_06.txt')
