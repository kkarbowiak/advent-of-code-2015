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


def day3_2():
    santa_pos = 0 + 0j
    robo_pos = 0 + 0j
    houses = set()
    houses.add(santa_pos)
    houses.add(robo_pos)

    santa_turn = True

    with open('data/03') as data:
        for lines in data:
            for ch in lines:
                if santa_turn:
                    santa_pos += get_shift_from_instruction(ch)
                    houses.add(santa_pos)
                    santa_turn = False
                else:
                    robo_pos += get_shift_from_instruction(ch)
                    houses.add(robo_pos)
                    santa_turn = True

    print('houses =', len(houses))


day3_1()
day3_2()
