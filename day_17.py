'''
--- Day 17: No Such Thing as Too Much ---

The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5
Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?
'''


def store(containers, liters, used=()):
    if liters == 0:
        yield used
    else:
        for i, container in enumerate(containers):
            if container <= liters:
                yield from store(
                    containers[i + 1:],
                    liters - container,
                    used + (container,)
                )


def read_instructions(file):
    with open(file) as f:
        instructions = list(map(int, f.readlines()))

    storage = list(store(instructions, 150))
    print(len(storage))


read_instructions('inputs/day_17.txt')
