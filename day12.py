import re
import json


def get_sum(json):
    sum = 0
    number = re.compile('-?[0-9]+')
    for f in number.findall(json):
        sum += int(f)

    return sum


def should_remove(object):
    return type(object) == type({}) and 'red' in object.values()


def remove_red_objects(object):
    if type(object) == type([]):
        i = 0
        size = len(object)
        while i < size:
            remove_red_objects(object[i])

            if should_remove(object[i]):
                del object[i]
                size -= 1
            else:
                i += 1
            
    elif type(object) == type({}):
        for k, v in list(object.items()):
            remove_red_objects(v)

            if should_remove(v):
                del object[k]


def day12_1():
    with open('data/12') as data:
        json = data.readline()

        sum = get_sum(json)

        print('sum =', sum)


def day12_2():
    with open('data/12') as data:
        object = json.load(data)
        remove_red_objects(object)

        dump = json.dumps(object)
        sum = get_sum(dump)

        print('sum =', sum)


day12_1()
day12_2()
