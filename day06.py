import re


def turn_on(light):
    return True


def turn_off(light):
    return False


def toggle(light):
    return light ^ True


def get_decoded_instruction(line):
    m = re.match('(turn on|turn off|toggle) ([0-9]+)\,([0-9]+) through ([0-9]+)\,([0-9]+)', line)

    start = int(m.group(2)), int(m.group(3))
    end = int(m.group(4)), int(m.group(5))

    if line.startswith('turn on'):
        return turn_on, start, end
    elif line.startswith('turn off'):
        return turn_off, start, end
    else:
        return toggle, start, end


def perform(lights, action, start, end):
    for y in range(start[1], end[1] + 1):
        for x in range(start[0], end[0] + 1):
            lights[x][y] = action(lights[x][y])


def count_lit(lights):
    count = 0

    for y in lights:
        for x in y:
            if x:
                count += 1

    return count


def day6_1():
    lights = [[False for x in range(1000)] for y in range(1000)]

    with open('data/06') as data:
        for line in data:
            action, start, stop = get_decoded_instruction(line)

            perform(lights, action, start, stop)

    num_lit = count_lit(lights)
    print('lit =', num_lit)


day6_1()
