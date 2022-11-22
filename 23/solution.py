with open('input.txt') as f:
    data = f.read()

data = data.replace(',', '')

instructions = [tuple(line.split()) for line in data.splitlines()]

def run(instructions, reg):
    i = 0
    while i < len(instructions):
        inst = instructions[i]
        if inst[0] == 'hlf':
            reg[inst[1]] /= 2
        elif inst[0] == 'tpl':
            reg[inst[1]] *= 3
        elif inst[0] == 'inc':
            reg[inst[1]] += 1
        elif inst[0] == 'jmp':
            i += int(inst[1])
            continue
        elif inst[0] == 'jie':
            if reg[inst[1]] % 2 == 0:
                i += int(inst[2])
                continue
        elif inst[0] == 'jio':
            if reg[inst[1]] == 1:
                i += int(inst[2])
                continue
        else:
            raise Exception(f"Invalid instruction {inst}")
        i += 1
    return reg['b']


print("Part 1:", run(instructions, {'a':0, 'b':0}))
print("Part 2:", run(instructions, {'a':1, 'b':0}))
