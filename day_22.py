from copy import deepcopy
import math
from collections import OrderedDict

spells = OrderedDict([
    ('magic_missile', 53),
    ('drain', 73),
    ('shield', 113),
    ('poison', 173),
    ('recharge', 229),
])

spells = {
    'magic_missile': 53,
    'drain': 73,
    'shield': 113,
    'poison': 173,
    'recharge': 229,
}

spells_symbols = {
    'magic_missile': '!',
    'drain': '@',
    'shield': '#',
    'poison': '$',
    'recharge': '%',
}

magic_effects = {
    'shield': {'armor': 7},
    'poison': {'boss_hp': -3},
    'recharge': {'mana': 101}
}


class BossDead(Exception): pass
class PlayerDead(Exception): pass


debug = False
def trace(s, state):
    if debug:
        i = ''.join(x[0] for x in state.chain)
        print(i, s)


class State(object):

    def __init__(self):
        self.__dict__.update(
            mana=500,
            mana_spent=0,
            player_hp=50,
            armor=0,
            boss_hp=51,
            boss_damage=9,
            effects={},
            chain=[],
        )

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        if name in ('player_hp', 'boss_hp'):
            self.check_outcome()

    def __getitem__(self, index):
        return self.__dict__[index]

    def __setitem__(self, index, value):
        self.__dict__[index] = value
        if index in ('player_hp', 'boss_hp'):
            self.check_outcome()

    def __repr__(self):
        return '<State: {}>'.format(str(self.__dict__))

    def check_outcome(self):
        if self.boss_hp <= 0:
            raise BossDead(str(self))
        elif self.player_hp <= 0:
            raise PlayerDead(str(self))


def apply_effects(state):
    effects = deepcopy(state.effects)
    state.armor = 0
    for effect in effects:
        for stat, change in magic_effects[effect].items():
            trace('{effect} provides {change} {stat}; its timer is now {timer}.'.format(
                effect=effect.title(), change=change, stat=stat, timer=state.effects[effect] - 1
                ), state)
            state[stat] += change
        state.effects[effect] -= 1
        if state.effects[effect] == 0:
            trace('{effect} wears off.'.format(effect=effect.title()), state)
            del state.effects[effect]
    return state


def player_move(state):
    cast = state.chain[-1]
    state.mana -= spells[cast]
    state.mana_spent += spells[cast]

    if cast == 'magic_missile':
        state.boss_hp -= 4
    elif cast == 'drain':
        state.player_hp += 2
        state.boss_hp -= 2
    elif cast == 'shield':
        state.effects['shield'] = 6
    elif cast == 'poison':
        state.effects['poison'] = 6
    elif cast == 'recharge':
        state.effects['recharge'] = 5
    return state


def boss_move(state):
    state.player_hp -= max(1, state.boss_damage - state.armor)
    return state


def available_spells(state):
    return [s for s in spells if state.mana >= spells[s] and state.effects.get(s, 0) <= 1]


def simulate(state):
    if state.mana_spent >= best - min(spells.values()):
        return
    try:
        if state.hard:
            state.player_hp -= 1

        state = apply_effects(state)
        state = player_move(state)
        state.check_outcome()

        state = apply_effects(state)
        state = boss_move(state)
        state.check_outcome()
    except PlayerDead:
        yield False, state
    except BossDead:
        print(best, '+', ''.join(spells_symbols[x] for x in state.chain), len(wins))
        yield True, state
    else:
        for spell in available_spells(state):
            xstate = deepcopy(state)
            xstate.chain.append(spell)
            yield from simulate(xstate)


def replay(chain, hard=False):
    state = State()
    state.hard = hard
    for n, spell in enumerate(chain, 1):
        trace('\n-- Player turn --', state)
        trace('- Player has {player_hp} hit points, {armor} armor, {mana} mana'.format_map(state), state)
        trace('- Boss has {boss_hp} hit points'.format_map(state), state)
        trace('Player casts {spell}.'.format(spell=spell.title()), state)
        state.chain.append(spell)
        if state.hard:
            state.player_hp -= 1

        state = apply_effects(state)
        state = player_move(state)
        state.check_outcome()

        trace('\n-- Boss turn --', state)
        trace('- Player has {player_hp} hit points, {armor} armor, {mana} mana'.format_map(state), state)
        trace('- Boss has {boss_hp} hit points'.format_map(state), state)
        state = apply_effects(state)
        state = boss_move(state)
        state.check_outcome()


def wizard_simulator_20xx(hard=False):
    '''yield every possible outcome'''
    for spell in spells:
        state = State()
        state.hard = hard
        state.chain.append(spell)
        yield from simulate(state)


wins = []
best = math.inf

for win, state in wizard_simulator_20xx(False):
    if win:
        wins.append(state.mana_spent)
    if wins and min(wins) < best:
        best = min(wins)

print(best)
