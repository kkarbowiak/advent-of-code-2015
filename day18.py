import copy


def get_decoded_light_row(line):
    row = []

    for ch in line:
        if ch == '.':
            row.append(False)
        elif ch == '#':
            row.append(True)

    return row


def count_lit(lights):
    count = 0

    for y in lights:
        for x in y:
            if x:
                count += 1

    return count


def count_lit_neighbours(lights, y, x):
    count = 0

    for y1 in range(max(0, y - 1), min(len(lights), y + 1 + 1)):
        for x1 in range(max(0, x - 1), min(len(lights[y1]), x + 1 + 1)):
            if not (y1 == y and x1 == x):
                if lights[y1][x1]:
                    count += 1

    return count


def get_next_state(lights, y, x):
    lit_neighbours = count_lit_neighbours(lights, y, x)
    if lights[y][x]:
        return lit_neighbours == 2 or lit_neighbours == 3
    else:
        return lit_neighbours == 3


def process_lights(lights):
    l2 = copy.deepcopy(lights)

    for y in range(len(lights)):
        for x in range(len(lights[y])):
            l2[y][x] = get_next_state(lights, y, x)

    return l2


def day18_1():
    lights = []
    with open('data/18') as data:
        for line in data:
            light_row = get_decoded_light_row(line)
            lights.append(light_row)

    for i in range(100):
        lights = process_lights(lights)

    num_lit = count_lit(lights)
    print('lit =', num_lit)


day18_1()
