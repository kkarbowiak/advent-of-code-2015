import collections
import re
import copy


Spell = collections.namedtuple('Spell', 'name cost damage heal armor mana effect')
Boss = collections.namedtuple('Boss', 'hp damage')
Player = collections.namedtuple('Player', 'hp mana')


class Effect:
    def __init__(self, spell, timer):
        self.spell = spell
        self.timer = timer


class State:
    def __init__(self, hp_player, mana_player, hp_boss, effects, mana_used):
        self.hp_player = hp_player
        self.mana_player = mana_player
        self.armor_player = 0
        self.hp_boss = hp_boss
        self.effects = effects
        self.mana_used = mana_used


def get_spells():
    return [
        Spell('Magic Missile', 53, 4, 0, 0, 0, None),
        Spell('Drain', 73, 2, 2, 0, 0, None),
        Spell('Shield', 113, 0, 0, 7, 0, 6),
        Spell('Poison', 173, 3, 0, 0, 0, 6),
        Spell('Recharge', 229, 0, 0, 0, 101, 5)
    ]


def get_player():
    return Player(50, 500)


def get_boss():
    b_hp = 0
    b_dmg = 0
    with open('data/22') as data:
        b_hp = get_decoded_value(data.readline())
        b_dmg = get_decoded_value(data.readline())

    return Boss(b_hp, b_dmg)


def get_decoded_value(line):
    m = re.match('\D+(\d+)', line)
    return int(m.group(1))


def get_possible_spells(spells, mana_left, effects):
    result = []

    for spell in spells:
        if spell.cost <= mana_left and not is_spell_in_effect(spell, effects):
            result.append(spell)

    return result


def is_spell_in_effect(spell, effects):
    result = False

    for effect in effects:
        if effect.spell.name == spell.name:
            result = True
            break

    return result


def process_effects(state):
    state.armor_player = 0

    for effect in state.effects:
        state.hp_player += effect.spell.heal
        state.hp_boss -= effect.spell.damage
        state.mana_player += effect.spell.mana
        state.armor_player += effect.spell.armor
        effect.timer -= 1

    state.effects = [e for e in state.effects if e.timer > 0]


def is_boss_dead(state):
    return state.hp_boss <= 0


def is_player_dead(state):
    return state.hp_player <= 0


def process_player_turn(state, spell):
    state.hp_player += spell.heal
    state.mana_player -= spell.cost
    state.mana_used += spell.cost

    if spell.effect:
        state.effects.append(Effect(spell, spell.effect))
    else:
        state.hp_boss -= spell.damage


def process_boss_turn(state, boss):
    damage = max(1, boss.damage - state.armor_player)
    state.hp_player -= damage


def day22_1():
    boss = get_boss()
    player = get_player()
    spells = get_spells()

    min_mana_used = 999999999999
    sequence = []

    game_states = [State(player.hp, player.mana, boss.hp, [], 0)]

    while game_states:
        state = game_states.pop()

        if state.mana_used < min_mana_used:
            process_effects(state)
            if is_boss_dead(state):
                min_mana_used = min(state.mana_used, min_mana_used)
                continue

            possible_spells = get_possible_spells(spells, state.mana_player, state.effects)

            for ps in possible_spells:
                new_state = copy.deepcopy(state)

                process_player_turn(new_state, ps)

                if is_boss_dead(new_state):
                    min_mana_used = min(new_state.mana_used, min_mana_used)
                    continue

                process_effects(new_state)
                if is_boss_dead(new_state):
                    min_mana_used = min(new_state.mana_used, min_mana_used)
                    continue

                process_boss_turn(new_state, boss)

                if is_boss_dead(new_state):
                    min_mana_used = min(new_state.mana_used, min_mana_used)
                    continue
                elif is_player_dead(new_state):
                    continue
                else:
                    game_states.append(new_state)


    print('mmana =', min_mana_used)


def day22_2():
    boss = get_boss()
    player = get_player()
    spells = get_spells()

    min_mana_used = 999999999999
    sequence = []

    game_states = [State(player.hp, player.mana, boss.hp, [], 0)]

    while game_states:
        state = game_states.pop()

        if state.mana_used < min_mana_used:
            state.hp_player -= 1
            if is_player_dead(state):
                continue

            process_effects(state)
            if is_boss_dead(state):
                min_mana_used = min(state.mana_used, min_mana_used)
                continue

            possible_spells = get_possible_spells(spells, state.mana_player, state.effects)

            for ps in possible_spells:
                new_state = copy.deepcopy(state)

                process_player_turn(new_state, ps)

                if is_boss_dead(new_state):
                    min_mana_used = min(new_state.mana_used, min_mana_used)
                    continue

                process_effects(new_state)
                if is_boss_dead(new_state):
                    min_mana_used = min(new_state.mana_used, min_mana_used)
                    continue

                process_boss_turn(new_state, boss)

                if is_boss_dead(new_state):
                    min_mana_used = min(new_state.mana_used, min_mana_used)
                    continue
                elif is_player_dead(new_state):
                    continue
                else:
                    game_states.append(new_state)


    print('mmana =', min_mana_used)


day22_1()
day22_2()
