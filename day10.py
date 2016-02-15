def look_and_say(text):
    result = ''

    len = 0
    char = text[0]

    for ch in text:
        if ch == char:
            len += 1
        else:
            result += str(len)
            result += char
            len = 1
            char = ch

    result += str(len)
    result += char

    return result


def day10_1():
    with open('data/10') as data:
        text = data.readline()

        for i in range(40):
            text = look_and_say(text)

        print('len =', len(text))


day10_1()
