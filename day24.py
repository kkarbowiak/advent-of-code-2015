import functools
import operator
import itertools
import copy


def get_weight(group):
    return functools.reduce(operator.add, group)


def get_qe(group):
    return functools.reduce(operator.mul, group)


def day24_1():
    items = []
    with open('data/24') as data:
        for line in data:
            items.append(int(line))

    min_qe = 999999999999

    found =  False

    for g1len in range(1, len(items) - 1):
        for g1 in itertools.combinations(items, g1len):
            g2g3 = [i for i in items if i not in g1]
            if get_weight(g2g3) == 2 * get_weight(g1):
                min_qe = min(min_qe, get_qe(g1))
                found = True
        if found:
            break

    print('min_qe =', min_qe)


day24_1()
