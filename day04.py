import hashlib


def get_digest(secret, noonce):
    text = secret + str(noonce)

    return hashlib.md5(str.encode(text)).hexdigest()


def starts_with_5_or_more_zeros(digest):
    return digest.startswith('00000')


def day4_1():
    with open('data/04') as data:
        secret = data.readline()
        noonce = 0
        hex = get_digest(secret, noonce)
        while not starts_with_5_or_more_zeros(hex):
            noonce += 1
            hex = get_digest(secret, noonce)

        print('noonce =', noonce)


def day4_2():
    with open('data/04') as data:
        secret = data.readline()
        noonce = 0
        hex = get_digest(secret, noonce)
        while not hex.startswith('000000'):
            noonce += 1
            hex = get_digest(secret, noonce)

        print('noonce =', noonce)


day4_1()
day4_2()
