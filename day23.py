class CPU:
    def __init__(self, a, b):
        self.regs = {'a': a, 'b': b}
        self.pc = 0


def process(cpu, program):
    instr = program[cpu.pc]
    if instr.startswith('hlf'):
        cpu.regs[instr[-1]] /= 2
        cpu.pc += 1
    elif instr.startswith('tpl'):
        cpu.regs[instr[-1]] *= 3
        cpu.pc += 1
    elif instr.startswith('inc'):
        cpu.regs[instr[-1]] += 1
        cpu.pc += 1
    elif instr.startswith('jmp'):
        cpu.pc += int(instr[4:])
    elif instr.startswith('jie'):
        if cpu.regs[instr[4]] % 2 == 0:
            cpu.pc += int(instr[7:])
        else:
            cpu.pc += 1
    elif instr.startswith('jio'):
        if cpu.regs[instr[4]] == 1:
            cpu.pc += int(instr[7:])
        else:
            cpu.pc += 1

    return not (0 <= cpu.pc < len(program))


def day23_1():
    program = []

    with open('data/23') as data:
        for line in data:
            program.append(line.strip())

    cpu = CPU(0, 0)

    terminated = False

    while not terminated:
        terminated = process(cpu, program)

    print('b =', cpu.regs['b'])


def day23_2():
    program = []

    with open('data/23') as data:
        for line in data:
            program.append(line.strip())

    cpu = CPU(1, 0)

    terminated = False

    while not terminated:
        terminated = process(cpu, program)

    print('b =', cpu.regs['b'])


day23_1()
day23_2()
