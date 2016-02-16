import re


def get_sum(json):
    sum = 0
    number = re.compile('-?[0-9]+')
    for f in number.findall(json):
        sum += int(f)

    return sum


def day12_1():
    with open('data/12') as data:
        json = data.readline()

        sum = get_sum(json)

        print('sum =', sum)


day12_1()
