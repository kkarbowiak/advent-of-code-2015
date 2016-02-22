import re


def get_decoded_replacement_or_molecule(line):
    regexp = re.compile('([a-zA-Z]+) => ([a-zA-Z]+)')
    m = regexp.match(line)
    if m:
        return (m.group(1), m.group(2)), None
    else:
        return None, line.strip()


def get_molecules_count(molecule, replacements):
    molecules = set()

    for (fr, tos) in replacements.items():
        if fr in molecule:
            index = 0
            while True:
                index = molecule.find(fr, index)
                if index == -1:
                    break

                for to in tos:
                    new_molecule = molecule[0:index] + to + molecule[index + len(fr):]
                    molecules.add(new_molecule)

                index += 1

    return len(molecules)


def get_new_molecules(molecule, replacements):
    result = set()

    for (fr, to) in replacements:
        index = 0
        while True:
            index = molecule.find(fr, index)
            if index == -1:
                break

            new_molecule = molecule[0:index] + to + molecule[index + len(fr):]
            result.add(new_molecule)

            index += 1

    return sorted(result)


def get_lowest_replacements_count(base, molecule, replacements):
    molecules = [(base, 0)]
    result = 0

    while molecules and result == 0:
        mol, count = molecules.pop()
        for new in get_new_molecules(mol, replacements):
            if new == molecule:
                result = count + 1
                break
            else:
                molecules.append((new, count + 1))

    return result


def day19_1():
    replacements = {}
    molecule = ''
    with open('data/19') as data:
        for line in data:
            replacement, molecule = get_decoded_replacement_or_molecule(line)
            if replacement is not None:
                fr = replacement[0]
                to = replacement[1]
                if fr in replacements:
                    replacements[fr].append(to)
                else:
                    replacements[fr] = [to]

    count = get_molecules_count(molecule, replacements)
    print('mcount =', count)


def day19_2():
    replacements = []
    molecule = ''
    with open('data/19') as data:
        for line in data:
            replacement, molecule = get_decoded_replacement_or_molecule(line)
            if replacement is not None:
                fr = replacement[1]
                to = replacement[0]
                replacements.append((fr, to))

    count = get_lowest_replacements_count(molecule, 'e', replacements)
    print('rcount =', count)


day19_1()
day19_2()

