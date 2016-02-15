def has_consecutive_doubles(line):
    result = False

    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            result = True
            break

    return result


def has_separated_doubles(line):
    result = False

    for i in range(len(line) - 2):
        if line[i] == line[i + 2]:
            result = True
            break

    return result


def has_doubled_pairs(line):
    result = False

    for i in range(len(line) - 1):
        if line.count(line[i : i + 2]) > 1:
            result = True
            break

    return result


def is_nice(line):
    nice = True
    if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
        nice = False
    elif line.count('a') + line.count('e') + line.count('i') + line.count('o') + line.count('u') < 3:
        nice = False
    elif not has_consecutive_doubles(line):
        nice = False

    return nice


def is_nice2(line):
    return has_separated_doubles(line) and has_doubled_pairs(line)


def day5_1():
    nice_count = 0

    with open('data/05') as data:
        for lines in data:
            if is_nice(lines):
                nice_count += 1

    print('nice = ', nice_count)


def day5_2():
    nice_count = 0

    with open('data/05') as data:
        for lines in data:
            if is_nice2(lines):
                nice_count += 1

    print('nice = ', nice_count)


day5_1()
day5_2()
