import itertools


def day17_1():
    containers = []
    combinations = 0
    with open('data/17') as data:
        for line in data:
            containers.append(int(line))

    for count in range(1, len(containers)):
        for conts in itertools.combinations(containers, count):
            if sum(conts) == 150:
                combinations += 1

    print('conts =', combinations)


def day17_2():
    containers = []
    combinations = 0
    with open('data/17') as data:
        for line in data:
            containers.append(int(line))

    min_containers = len(containers)

    for count in range(1, len(containers)):
        for conts in itertools.combinations(containers, count):
            if sum(conts) == 150:
                min_containers = min(min_containers, count)

    for conts in itertools.combinations(containers, min_containers):
            if sum(conts) == 150:
                if sum(conts) == 150:
                    combinations += 1

    print('conts =', combinations)


day17_1()
day17_2()
