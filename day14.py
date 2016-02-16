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


def day14_2():
    speeds = []
    times = []
    rests = []
    scores = []
    distances = []
    with open('data/14') as data:
        for line in data:
            speed, time, rest = get_speed_time_rest_from_instruction(line)
            speeds.append(speed)
            times.append(time)
            rests.append(rest)
            scores.append(0)
            distances.append(0)

    for seconds in range(1, 2503 + 1):
        for i in range(len(speeds)):
            distances[i] = get_distance_after_time(speeds[i], times[i], rests[i], seconds)

        max_dist = max(distances)
        for i in range(len(distances)):
            if distances[i] == max_dist:
                scores[i] += 1

    print('mscore =', max(scores))


day14_1()
day14_2()
