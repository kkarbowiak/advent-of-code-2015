import re


def get_speed_time_rest_from_instruction(line):
    regexp = re.compile('[a-zA-Z]+ can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds.')
    m = regexp.match(line)
    return int(m.group(1)), int(m.group(2)), int(m.group(3))


def get_distance_after_time(speed, time, rest, after):
    period = time + rest
    quot = after // period
    rem = after % period

    return quot * time * speed + min(time, rem) * speed


def day14_1():
    max_dist = 0
    with open('data/14') as data:
        for line in data:
            speed, time, rest = get_speed_time_rest_from_instruction(line)
            dist = get_distance_after_time(speed, time, rest, 2503)
            max_dist = max(max_dist, dist)
    
    print('mdist =', max_dist)


day14_1()
