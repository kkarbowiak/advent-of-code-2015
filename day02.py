def get_lwh(line):
    list = line.split('x')
    return int(list[0]), int(list[1]), int(list[2])


def get_cuboid_area(l, w, h):
    return (2 * l * w + 2 * l * h + 2 * w * h)


def get_smallest_face_area(l, w, h):
    return min(l * w, l * h, w * h)


def get_smallest_face_perimeter(l, w, h):
    return min(2 * (l + w), 2 * (l + h), 2 * (w + h))


def day2_1():
    area = 0

    with open('data/02') as data:
        for lines in data:
            l, w, h = get_lwh(lines)
            area += get_cuboid_area(l, w, h)
            area += get_smallest_face_area(l, w, h)

    print('area =', area)


def day2_2():
    length = 0

    with open('data/02') as data:
        for lines in data:
            l, w, h = get_lwh(lines)
            length += get_smallest_face_perimeter(l, w, h)
            length += l * w * h

    print('length =', length)


day2_1()
day2_2()
