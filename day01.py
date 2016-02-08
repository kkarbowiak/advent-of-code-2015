def get_num_from_instruction(ch):
    if ch == '(':
        return 1
    elif ch == ')':
        return -1

def day1_1():
    floor = 0

    with open('data/01') as data:
        for lines in data:
            for ch in lines:
                floor += get_num_from_instruction(ch)

    print('floor =', floor)


def day1_2():
    floor = 0
    seq = 0

    with open('data/01') as data:
        for lines in data:
            if floor == -1:
                break
            for ch in lines:
                if floor == -1:
                    break
                floor += get_num_from_instruction(ch)
                seq += 1

    print('seq =', seq)

day1_1()
day1_2()
