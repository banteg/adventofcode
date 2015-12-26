from copy import copy
import math


boss_hp = 51
boss_damage = 9

spells = {
    'magic_missile': 53,
    'drain': 73,
    'shield': 113,
    'poison': 173,
    'recharge': 229,
}

magic_effects = {
    'shield': {'armor': 7},
    'poison': {'boss_hp': -3},
    'recharge': {'mana': 101}
}


class BossDead(Exception):
    pass


class PlayerDead(Exception):
    pass


class State(object):

    def __init__(self):
        self.__dict__.update(
            mana=500,
            mana_spent=0,
            player_hp=50,
            armor=0,
            boss_hp=boss_hp,
            boss_damage=boss_damage,
            effects={},
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

    def __copy__(self):
        new = State()
        new.__dict__.update(self.__dict__)
        new.effects = self.effects.copy()
        return new

    def check_outcome(self):
        if self.boss_hp <= 0:
            raise BossDead(str(self))
        elif self.player_hp <= 0:
            raise PlayerDead(str(self))


def apply_effects(state):
    effects = state.effects.copy()
    state.armor = 0
    for effect in effects:
        for stat, change in magic_effects[effect].items():
            state[stat] += change
        state.effects[effect] -= 1
        if state.effects[effect] == 0:
            del state.effects[effect]
    return state


def player_move(state):
    cast = state.spell
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
    if state.mana_spent >= best[state.hard] - spells[state.spell]:
        return
    try:
        if state.hard:
            state.player_hp -= 1

        state = apply_effects(state)
        state = player_move(state)

        state = apply_effects(state)
        state = boss_move(state)
    except PlayerDead:
        yield False, state
    except BossDead:
        best[state.hard] = state.mana_spent
        yield True, state
    else:
        for spell in available_spells(state):
            new = copy(state)
            new.spell = spell
            yield from simulate(new)


def wizard_simulator_20xx(hard=False):
    'yields every possible outcome'
    for spell in spells:
        state = State()
        state.hard = hard
        state.spell = spell
        yield from simulate(state)


def win_with_least_mana_spent(hard=False):
    list(wizard_simulator_20xx(hard))
    print(best[hard])
    return best[hard]


best = {True: math.inf, False: math.inf}
easy = win_with_least_mana_spent()
hard = win_with_least_mana_spent(hard=True)
