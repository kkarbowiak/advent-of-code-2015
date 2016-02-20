import re


def get_decoded_replacement_or_molecule(line):
    regexp = re.compile('([a-zA-Z]+) => ([a-zA-Z]+)')
    m = regexp.match(line)
    if m:
        return (m.group(1), m.group(2)), None
    else:
        return None, line


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


day19_1()
