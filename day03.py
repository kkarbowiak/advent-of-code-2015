def get_shift_from_instruction(ch):
    if ch == '^':
        return 0 + 1j
    elif ch == 'v':
        return 0 - 1j
    elif ch == '<':
        return -1 + 0j
    elif ch == '>':
        return 1 + 0j


def day3_1():
    pos = 0 + 0j
    houses = set()
    houses.add(pos)

    with open('data/03') as data:
        for lines in data:
            for ch in lines:
                pos += get_shift_from_instruction(ch)
                houses.add(pos)

    print('houses =', len(houses))


day3_1()
