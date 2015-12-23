'''
--- Day 15: Science for Hungry People ---

Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

capacity (how well it helps the cookie absorb milk)
durability (how well it keeps the cookie intact when full of milk)
flavor (how tasty it makes the cookie)
texture (how it improves the feel of the cookie)
calories (how many calories it adds to the cookie)
You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

A capacity of 44*-1 + 56*2 = 68
A durability of 44*-2 + 56*3 = 80
A flavor of 44*6 + 56*-2 = 152
A texture of 44*3 + 56*-1 = 76
Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?
'''

import re
from collections import namedtuple

Ingredient = namedtuple('Ingredient', ['name', 'capacity', 'durability', 'flavor', 'texture', 'calories'])
ingredient = re.compile(r'(.*): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')


def parse_ingredient(s):
    name, *properties = ingredient.search(s).groups()
    properties = map(int, properties)
    return Ingredient(name, *properties)


def get_score(ingredients, counts):
    capacity = max(sum(i.capacity * counts[c] for c, i in enumerate(ingredients)), 0)
    durability = max(sum(i.durability * counts[c] for c, i in enumerate(ingredients)), 0)
    flavor = max(sum(i.flavor * counts[c] for c, i in enumerate(ingredients)), 0)
    texture = max(sum(i.texture * counts[c] for c, i in enumerate(ingredients)), 0)
    score = capacity * durability * flavor * texture
    return score


def cook(ingredients):
    best = 0
    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - b):
                d = 100 - a - b - c
                score = get_score(ingredients, (a, b, c, d))
                best = max(score, best)

    print(best)
    return best


def read_instructions(file):
    with open(file) as f:
        ingredients = list(map(parse_ingredient, f.readlines()))

    cook(ingredients)


read_instructions('inputs/day_15.txt')
