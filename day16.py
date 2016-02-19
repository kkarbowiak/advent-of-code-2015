import re


class Sue:
    def __init__(self, number):
        self.number = number
        self.children = None
        self.cats = None
        self.samoyeds = None
        self.pomeranians = None
        self.akitas = None
        self.vizslas = None
        self.goldfish = None
        self.trees = None
        self.cars = None
        self.cars = None

    def __repr__(self):
        return '`{0}.{1}.{2}.{3}.{4}.{5}.{6}.{7}.{8}.{9}.{10}`'.format(self.number, self.children, self.cats, self.samoyeds, self.pomeranians, self.akitas, self.vizslas, self.goldfish, self.trees, self.cars, self.cars)


def get_value(line, regexp):
    m = regexp.match(line)
    if m:
        return int(m.group(1))
    else:
        return None


def get_decoded_sue(line):
    number_re = re.compile('Sue ([0-9]+)\:.*')
    children_re = re.compile('.+children\: ([0-9]+).*')
    cats_re = re.compile('.+cats\: ([0-9]+).*')
    samoyeds_re = re.compile('.+samoyeds\: ([0-9]+).*')
    pomeranians_re = re.compile('.+pomeranians\: ([0-9]+).*')
    akitas_re = re.compile('.+akitas\: ([0-9]+).*')
    vizslas_re = re.compile('.+vizslas\: ([0-9]+).*')
    goldfish_re = re.compile('.+goldfish\: ([0-9]+).*')
    trees_re = re.compile('.+trees\: ([0-9]+).*')
    cars_re = re.compile('.+cars\: ([0-9]+).*')
    perfumes_re = re.compile('.+perfumes\: ([0-9]+).*')

    m = number_re.match(line)
    sue = Sue(int(m.group(1)))

    sue.children = get_value(line, children_re)
    sue.cats = get_value(line, cats_re)
    sue.samoyeds = get_value(line, samoyeds_re)
    sue.pomeranians = get_value(line, pomeranians_re)
    sue.akitas = get_value(line, akitas_re)
    sue.vizslas = get_value(line, vizslas_re)
    sue.goldfish = get_value(line, goldfish_re)
    sue.trees = get_value(line, trees_re)
    sue.cars = get_value(line, cars_re)
    sue.perfumes = get_value(line, perfumes_re)

    return sue


def matches_MFCSAM(sue):
    return ((sue.children is None or sue.children == 3)
        and (sue.cats is None or sue.cats == 7)
        and (sue.samoyeds is None or sue.samoyeds == 2)
        and (sue.pomeranians is None or sue.pomeranians == 3)
        and (sue.akitas is None or sue.akitas == 0)
        and (sue.vizslas is None or sue.vizslas == 0)
        and (sue.goldfish is None or sue.goldfish == 5)
        and (sue.trees is None or sue.trees == 3)
        and (sue.cars is None or sue.cars == 2)
        and (sue.perfumes is None or sue.perfumes == 1))



def matches_MFCSAM_2(sue):
    return ((sue.children is None or sue.children == 3)
        and (sue.cats is None or sue.cats > 7)
        and (sue.samoyeds is None or sue.samoyeds == 2)
        and (sue.pomeranians is None or sue.pomeranians < 3)
        and (sue.akitas is None or sue.akitas == 0)
        and (sue.vizslas is None or sue.vizslas == 0)
        and (sue.goldfish is None or sue.goldfish < 5)
        and (sue.trees is None or sue.trees > 3)
        and (sue.cars is None or sue.cars == 2)
        and (sue.perfumes is None or sue.perfumes == 1))


def day16_1():
    sues = []
    with open('data/16') as data:
        for line in data:
            sue = get_decoded_sue(line)
            sues.append(sue)

    filtered = [s for s in sues if matches_MFCSAM(s)]

    print('sue =', filtered)


def day16_2():
    sues = []
    with open('data/16') as data:
        for line in data:
            sue = get_decoded_sue(line)
            sues.append(sue)

    filtered = [s for s in sues if matches_MFCSAM_2(s)]

    print('sue =', filtered)


day16_1()
day16_2()
