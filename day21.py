import re
import collections
import itertools
import math


Character = collections.namedtuple('Character', 'hp dmg arm')
Item = collections.namedtuple('Item', 'name gold dmg arm')


def get_decoded_value(line):
    m = re.match('\D+(\d+)', line)
    return int(m.group(1))


def get_boss():
    b_hp = 0
    b_dmg = 0
    b_arm = 0
    with open('data/21') as data:
        b_hp = get_decoded_value(data.readline())
        b_dmg = get_decoded_value(data.readline())
        b_arm = get_decoded_value(data.readline())

    return Character(b_hp, b_dmg, b_arm)


def get_player(items):
    dmg = sum(i.dmg for i in items)
    arm = sum(i.arm for i in items)
    return Character(100, dmg, arm)


def get_weapons():
    return [
        Item('Dagger', 8, 4, 0),
        Item('Shortsword', 10, 5, 0),
        Item('Warhammer', 25, 6, 0),
        Item('Longsword', 40, 7, 0),
        Item('Greataxe', 74, 8, 0)
    ]


def get_armors():
    return [
        Item('Leather', 13, 0, 1),
        Item('Chainmail', 31, 0, 2),
        Item('Splintmail', 53, 0, 3),
        Item('Bandedmail', 75, 0, 4),
        Item('Platemail', 102, 0, 5)
    ]


def get_rings():
    return [
        Item('Damage_1', 25, 1, 0),
        Item('Damage_2', 50, 2, 0),
        Item('Damage_3', 100, 3, 0),
        Item('Defense_1', 20, 0, 1),
        Item('Defense_2', 40, 0, 2),
        Item('Defense_3', 80, 0, 3)
    ]


def get_cost(items):
    return sum(i.gold for i in items)


def does_player_win(player, boss):
    player_attack = max(player.dmg - boss.arm, 1)
    boss_attack = max(boss.dmg - player.arm, 1)
    boss_die_turn = math.ceil(boss.hp / player_attack)
    player_die_turn = math.ceil(player.hp / boss_attack)
    return boss_die_turn <= player_die_turn


def day21_1():
    boss = get_boss()

    weapons = get_weapons()
    armors = get_armors()
    rings = get_rings()

    min_cost = 999999999999

    for w in itertools.combinations(weapons, 1):
        for a_c in range(0, 2):
            for a in itertools.combinations(armors, a_c):
                for r_c in range(0, 3):
                    for r in itertools.combinations(rings, r_c):
                        items = list(w) + list(a) + list(r)
                        player = get_player(items)
                        if does_player_win(player, boss):
                            min_cost = min(min_cost, get_cost(items))

    print('mcost =', min_cost)


def day21_2():
    boss = get_boss()

    weapons = get_weapons()
    armors = get_armors()
    rings = get_rings()

    max_cost = 0

    for w in itertools.combinations(weapons, 1):
        for a_c in range(0, 2):
            for a in itertools.combinations(armors, a_c):
                for r_c in range(0, 3):
                    for r in itertools.combinations(rings, r_c):
                        items = list(w) + list(a) + list(r)
                        player = get_player(items)
                        if not does_player_win(player, boss):
                            max_cost = max(max_cost, get_cost(items))

    print('mcost =', max_cost)


day21_1()
day21_2()
