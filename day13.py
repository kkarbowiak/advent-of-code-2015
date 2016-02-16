import re
import itertools


def get_happiness_from_instruction(line):
    regexp = re.compile('([a-zA-Z]+) would (gain|lose) ([0-9]+) happiness units by sitting next to ([a-zA-Z]+)\.')
    m = regexp.match(line)
    if m.group(2) == 'gain':
        return m.group(1), m.group(4), int(m.group(3))
    elif m.group(2) == 'lose':
        return m.group(1), m.group(4), -int(m.group(3))


def day13_1():
    happinesses = {}
    people = set()
    max_happiness = -999999999999
    with open('data/13') as data:
        for line in data:
            n1, n2, happiness = get_happiness_from_instruction(line)
            happinesses[n1, n2] = happiness
            people.add(n1)
            people.add(n2)

        for order in itertools.permutations(people):
            score = 0
            for index in range(len(order)):
                next = (index + 1) % len(order)
                score += happinesses[order[index], order[next]]
                score += happinesses[order[next], order[index]]
            max_happiness = max(max_happiness, score)

    print('happiness =', max_happiness)


day13_1()
