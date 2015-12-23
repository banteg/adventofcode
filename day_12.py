'''
--- Day 12: JSAbacusFramework.io ---

Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

For example:

[1,2,3] and {"a":2,"b":4} both have a sum of 6.
[[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
{"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
[] and {} both have a sum of 0.
You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?
'''

import json


with open('inputs/day_12.txt') as f:
    data = json.load(f)


def flatten(x):
    if isinstance(x, dict):
        for i in x.values():
            yield from flatten(i)
    elif isinstance(x, list):
        for i in x:
            yield from flatten(i)
    elif isinstance(x, int):
        yield x


result = sum(flatten(data))
print(result)
