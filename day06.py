import re


def turn_on(light):
    return True


def turn_off(light):
    return False


def toggle(light):
    return light ^ True


def turn_on2(light):
    return light + 1


def turn_off2(light):
    return max(0, light - 1)


def toggle2(light):
    return light + 2


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


def get_decoded_instruction2(line):
    m = re.match('(turn on|turn off|toggle) ([0-9]+)\,([0-9]+) through ([0-9]+)\,([0-9]+)', line)

    start = int(m.group(2)), int(m.group(3))
    end = int(m.group(4)), int(m.group(5))

    if line.startswith('turn on'):
        return turn_on2, start, end
    elif line.startswith('turn off'):
        return turn_off2, start, end
    else:
        return toggle2, start, end


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


def count_brightness(lights):
    brightness = 0

    for y in lights:
        for x in y:
            brightness += x

    return brightness


def day6_1():
    lights = [[False for x in range(1000)] for y in range(1000)]

    with open('data/06') as data:
        for line in data:
            action, start, stop = get_decoded_instruction(line)

            perform(lights, action, start, stop)

    num_lit = count_lit(lights)
    print('lit =', num_lit)


def day6_2():
    lights = [[0 for x in range(1000)] for y in range(1000)]

    with open('data/06') as data:
        for line in data:
            action, start, stop = get_decoded_instruction2(line)

            perform(lights, action, start, stop)

    brightness = count_brightness(lights)
    print('brightness =', brightness)


day6_1()
day6_2()
