def has_consecutive_doubles(line):
    result = False

    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
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


def day5_1():
    nice_count = 0

    with open('data/05') as data:
        for lines in data:
            if is_nice(lines):
                nice_count += 1

    print('nice = ', nice_count)


day5_1()
