import re


class Output:
    def getValue(self):
        raise NotImplementedError()
    

class Value(Output):
    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value


class Wire(Output):
    def __init__(self, wire):
        self.wire = wire

    def getValue(self):
        return getWireValue(self.wire)


class GateNOT(Output):
    def __init__(self, wire):
        self.wire = wire

    def getValue(self):
        return ~getWireValue(self.wire)


class GateOR(Output):
    def __init__(self, wire_a, wire_b):
        self.wire_a = wire_a
        self.wire_b = wire_b

    def getValue(self):
        return getWireValue(self.wire_a) | getWireValue(self.wire_b)


class GateORVal(Output):
    def __init__(self, wire_a, value):
        self.wire_a = wire_a
        self.value = value

    def getValue(self):
        return getWireValue(self.wire_a) | self.value


class GateAND(Output):
    def __init__(self, wire_a, wire_b):
        self.wire_a = wire_a
        self.wire_b = wire_b

    def getValue(self):
        return getWireValue(self.wire_a) & getWireValue(self.wire_b)


class GateANDVal(Output):
    def __init__(self, wire_a, value):
        self.wire_a = wire_a
        self.value = value

    def getValue(self):
        return getWireValue(self.wire_a) & self.value


class GateLSHIFT(Output):
    def __init__(self, wire, shift):
        self.wire = wire
        self.shift = shift

    def getValue(self):
        return getWireValue(self.wire) << self.shift


class GateRSHIFT(Output):
    def __init__(self, wire, shift):
        self.wire = wire
        self.shift = shift

    def getValue(self):
        return getWireValue(self.wire) >> self.shift


wire_to_output = {}
cache = {}

def getWireValue(wire):
    if wire in cache:
        return cache[wire]
    else:
        output = wire_to_output[wire]
        value = output.getValue()
        cache[wire] = value

    return value


def get_wire_and_output_from_instruction(line):
    value_re = re.compile('([0-9]+) -> ([a-zA-Z]+)')
    wire_re = re.compile('([a-zA-Z]+) -> ([a-zA-Z]+)')
    not_re = re.compile('NOT ([a-zA-Z]+) -> ([a-zA-Z]+)')
    or_re = re.compile('([a-zA-Z]+) OR ([a-zA-Z]+) -> ([a-zA-Z]+)')
    or_val1_re = re.compile('([0-9]+) OR ([a-zA-Z]+) -> ([a-zA-Z]+)')
    or_val2_re = re.compile('([a-zA-Z]+) OR ([0-9]+) -> ([a-zA-Z]+)')
    and_re = re.compile('([a-zA-Z]+) AND ([a-zA-Z]+) -> ([a-zA-Z]+)')
    and_val1_re = re.compile('([0-9]+) AND ([a-zA-Z]+) -> ([a-zA-Z]+)')
    and_val2_re = re.compile('([a-zA-Z]+) AND ([0-9]+) -> ([a-zA-Z]+)')
    lshift_re = re.compile('([a-zA-Z]+) LSHIFT ([0-9]+) -> ([a-zA-Z]+)')
    rshift_re = re.compile('([a-zA-Z]+) RSHIFT ([0-9]+) -> ([a-zA-Z]+)')

    m = value_re.match(line)
    if m:
        return m.group(2), Value(int(m.group(1)))

    m = wire_re.match(line)
    if m:
        return m.group(2), Wire(m.group(1))

    m = not_re.match(line)
    if m:
        return m.group(2), GateNOT(m.group(1))

    m = or_re.match(line)
    if m:
        return m.group(3), GateOR(m.group(1), m.group(2))

    m = or_val1_re.match(line)
    if m:
        return m.group(3), GateORVal(m.group(2), int(m.group(1)))

    m = or_val2_re.match(line)
    if m:
        return m.group(3), GateORVal(m.group(1), int(m.group(2)))

    m = and_re.match(line)
    if m:
        return m.group(3), GateAND(m.group(1), m.group(2))

    m = and_val1_re.match(line)
    if m:
        return m.group(3), GateANDVal(m.group(2), int(m.group(1)))

    m = and_val2_re.match(line)
    if m:
        return m.group(3), GateANDVal(m.group(1), int(m.group(2)))

    m = lshift_re.match(line)
    if m:
        return m.group(3), GateLSHIFT(m.group(1), int(m.group(2)))

    m = rshift_re.match(line)
    if m:
        return m.group(3), GateRSHIFT(m.group(1), int(m.group(2)))


def day7_1():
    with open('data/07') as data:
        for line in data:
            wire, output = get_wire_and_output_from_instruction(line)
            wire_to_output[wire] = output

    print('a =', getWireValue('a'))


day7_1()
