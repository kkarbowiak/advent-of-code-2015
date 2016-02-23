def day20_1():
    presents = None
    with open('data/20') as data:
        presents = int(data.readline())

    house = 0
    l = [0] * presents

    for i in range(1, presents + 1):
        j = i
        while j < presents:
            l[j] += 10 * i
            j += i

    for i in range(1, presents + 1):
        if l[i] >= presents:
            house = i
            break

    print('house =', house)


def day20_2():
    presents = None
    with open('data/20') as data:
        presents = int(data.readline())

    house = 0
    l = [0] * presents

    for i in range(1, presents + 1):
        j = i
        d = 0
        while j < presents and d < 50:
            l[j] += 11 * i
            j += i
            d += 1

    for i in range(1, presents + 1):
        if l[i] >= presents:
            house = i
            break

    print('house =', house)


day20_1()
day20_2()
