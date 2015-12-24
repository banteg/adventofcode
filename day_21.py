from collections import namedtuple
from itertools import combinations

Item = namedtuple('Item', ['name', 'cost', 'damage', 'armor'])
Player = namedtuple('Player', ['hp', 'cost', 'damage', 'armor', 'equipment'])
Boss = namedtuple('Boss', ['hp', 'damage', 'armor'])

weapons = {
    Item('Dagger', 8, 4, 0),
    Item('Shortsword', 10, 5, 0),
    Item('Warhammer', 25, 6, 0),
    Item('Longsword', 40, 7, 0),
    Item('Greataxe', 74, 8, 0),
}

armor = {
    Item('Leather', 13, 0, 1),
    Item('Chainmail', 31, 0, 2),
    Item('Splintmail', 53, 0, 3),
    Item('Bandedmail', 75, 0, 4),
    Item('Platemail', 102, 0, 5),
}

rings = {
    Item('Damage +1', 25, 1, 0),
    Item('Damage +2', 50, 2, 0),
    Item('Damage +3', 100, 3, 0),
    Item('Defense +1', 20, 0, 1),
    Item('Defense +2', 40, 0, 2),
    Item('Defense +3', 80, 0, 3),
}


def equip_player(equipment, hp=100):
    stats = [sum(x[y] for x in equipment) for y in (1, 2, 3)]
    return Player(hp, *stats, equipment)


def visit_shop():
    for armr in (0, 1):
        for ring in (0, 1, 2):
            for wc in combinations(weapons, 1):
                for ac in combinations(armor, armr):
                    for rc in combinations(rings, ring):
                        yield equip_player(wc + ac + rc)


def fight(player, boss):
    player = player._asdict()
    boss = boss._asdict()
    i = 0
    while True:
        if not i % 2:
            # player's move
            boss['hp'] -= max(player['damage'] - boss['armor'], 1)
            if boss['hp'] <= 0:
                return True
        else:
            player['hp'] -= max(boss['damage'] - player['armor'], 1)
            if player['hp'] <= 0:
                return False
        i += 1


def rpg_simulator_20xx():
    won = set()
    lost = set()
    for player in visit_shop():
        boss = Boss(hp=109, damage=8, armor=2)
        outcome = fight(player, boss)
        if outcome:
            won.add(player)
        else:
            lost.add(player)

    min_spent_and_won = min(won, key=lambda x: x.cost)
    max_spent_and_lost = max(lost, key=lambda x: x.cost)
    print(min_spent_and_won.cost)
    print(max_spent_and_lost.cost)


rpg_simulator_20xx()
