def increment(passw):
    increment_pos(passw, 7)


def increment_pos(passw, pos):
    passw[pos] += 1
    if passw[pos] > ord('z'):
        passw[pos] = ord('a')
        if pos > 0:
            increment_pos(passw, pos - 1)


def has_forbidden_chars(passw):
    return ord('i') in passw or ord('o') in passw or ord('l') in passw


def has_straight(passw):
    for i in range(len(passw) - 2):
        if (passw[i] + 1) == passw[i + 1] and (passw[i] + 2) == passw[i + 2]:
            return True
    else:
        return False


def has_pairs(passw):
    i = 0
    pairs = set()
    while i < (len(passw) - 1):
        if (passw[i] == passw[i + 1]):
            pairs.add(passw[i])
            i += 2
        else:
            i += 1

    return (len(pairs) > 1)


def is_valid(passw):
    if has_forbidden_chars(passw):
        return False
    elif not has_straight(passw):
        return False
    elif not has_pairs(passw):
        return False
    else:
        return True


def day11_1():
    with open('data/11') as data:
        passw = bytearray(data.readline().encode())

        increment(passw)
        while not is_valid(passw):
            increment(passw)

        print('pass =', passw)


day11_1()
