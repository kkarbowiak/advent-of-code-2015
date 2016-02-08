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


day1_1()
