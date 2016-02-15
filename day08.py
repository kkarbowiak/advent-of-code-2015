import re


def get_code_size(line):
    return len(line)


def get_folded_line(line):
    backslash = re.compile(r'\\\\')
    dquote = re.compile(r'\\"')
    hex = re.compile(r'\\x[0-9a-fA-F]{2}')
    folded = line[1:-1]
    folded = backslash.sub('?', folded)
    folded = dquote.sub('?', folded)
    folded = hex.sub('?', folded)
    return folded


def get_memory_size(line):
    folded_line = get_folded_line(line)
    return len(folded_line)


def day8_1():
    code = 0
    memory = 0

    with open('data/08') as data:
        for line in data:
            line = line.strip()
            code += get_code_size(line)
            memory += get_memory_size(line)

    print('diff =', code - memory)


day8_1()
