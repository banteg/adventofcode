from collections import defaultdict
from copy import deepcopy

spells = {
    'magic_missile': 53,
    'drain': 73,
    'shield': 113,
    'poison': 173,
    'recharge': 229,
}

magic_effects = {
    'shield': {'armor': 6},
    'poison': {'boss_hp': -3},
    'recharge': {'mana': 101}
}


def new_state():
    state = defaultdict(int)
    state.update({
        'mana': 500,
        'player_hp': 50,
        'boss_hp': 51,
        'boss_damage': 9,
        'effects': {},
        'n': 0,
        'chain': []
    })
    return state


def apply_effects(state):
    effects = deepcopy(state['effects'])
    state['armor'] = 0
    for effect in effects:
        for stat, change in magic_effects[effect].items():
            state[stat] += change
        state['effects'][effect] -= 1
        if state['effects'][effect] == 0:
            del state['effects'][effect]
    return state


def player_move(state):
    cast = state['chain'][-1]
    state['mana'] -= spells[cast]
    state['mana_spent'] += spells[cast]

    if cast == 'magic_missile':
        state['boss_hp'] -= 4
    elif cast == 'drain':
        state['player_hp'] += 2
        state['boss_hp'] -= 2
    elif cast == 'shield':
        state['effects']['shield'] = 6
    elif cast == 'poison':
        state['effects']['poison'] = 6
    elif cast == 'recharge':
        state['effects']['recharge'] = 6
    return state


def boss_move(state):
    state['player_hp'] -= max(state['boss_damage'] - state['armor'], 1)
    return state


def available_spells(state):
    return [s for s in spells if state['mana'] >= spells[s] and s not in state['effects']]


def simulate(state):
    state['n'] += 1
    state = apply_effects(state)
    state = player_move(state)
    if state['boss_hp'] <= 0:
        yield True, state['mana_spent']
        return

    state = apply_effects(state)
    state = boss_move(state)
    if state['player_hp'] <= 0:
        yield False, state['mana_spent']
        return

    for spell in available_spells(state):
        state['chain'].append(spell)
        yield from simulate(deepcopy(state))


def wizard_simulator_20xx():
    for spell in spells:
        state = new_state()
        state['chain'].append(spell)
        yield from simulate(state)


wins = [mana for win, mana in wizard_simulator_20xx() if win]
print(min(wins))
