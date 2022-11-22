with open('input.txt') as f:
    data = f.read()


ticker_tape = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""


real_sue = {}
for line in ticker_tape.splitlines():
    split = line.split(': ')
    real_sue[split[0]] = int(split[1])


for line in data.splitlines():
    split = line.replace(',', '').replace(':', '').split()

    potential_sue = {}
    potential_sue[split[2]] = int(split[3])
    potential_sue[split[4]] = int(split[5])
    potential_sue[split[6]] = int(split[7])

    if all((
        potential_sue[k] == real_sue[k]
        for k in potential_sue.keys()
    )):
        print("Part 1:", split[1])

    for k in potential_sue.keys():
        if k in ('cats', 'trees'):
            if not potential_sue[k] > real_sue[k]:
                break
        elif k in ('pomeranians', 'goldfish'):
            if not potential_sue[k] < real_sue[k]:
                break
        else:
            if not potential_sue[k] == real_sue[k]:
                break
    else:
        print("Part 2:", split[1])
