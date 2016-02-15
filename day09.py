import re
import itertools


def get_src_dst_dist_from_instruction(line):
    regexp = re.compile('([a-zA-Z]+)\sto\s([a-zA-Z]+)\s=\s([0-9]+)')
    m = regexp.match(line)
    return m.group(1), m.group(2), int(m.group(3))


def day9_1():
    distances = {}
    places = set()
    min_dist = 999999999999
    with open('data/09') as data:
        for line in data:
            src, dst, dist = get_src_dst_dist_from_instruction(line)
            distances[src, dst] = dist
            distances[dst, src] = dist
            places.add(src)
            places.add(dst)

    for order in itertools.permutations(places):
        dist = 0
        for index in range(len(order) - 1):
            dist += distances[order[index], order[index + 1]]
        min_dist = min(min_dist, dist)

    print('mdist =', min_dist)



def day9_2():
    distances = {}
    places = set()
    max_dist = 0
    with open('data/09') as data:
        for line in data:
            src, dst, dist = get_src_dst_dist_from_instruction(line)
            distances[src, dst] = dist
            distances[dst, src] = dist
            places.add(src)
            places.add(dst)

    for order in itertools.permutations(places):
        dist = 0
        for index in range(len(order) - 1):
            dist += distances[order[index], order[index + 1]]
        max_dist = max(max_dist, dist)

    print('mdist =', max_dist)

day9_1()
day9_2()
