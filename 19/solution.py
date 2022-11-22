import heapq
import re

with open('input.txt') as f:
    data = f.read()
    data1, data2 = data.split('\n\n')


rules = set()
for line in data1.splitlines():
    rules.add(tuple(line.split(' => ')))


molecules = set()
for rule in rules:
    p = re.compile(rule[0])
    indexes = [m.start() for m in p.finditer(data2)]
    for i in indexes:
        molecule = data2[:i] + rule[1] + data2[i + len(rule[0]):]
        molecules.add(molecule)

print("Part 1:", len(molecules))


visited = set()
q = [(0, 0, data2)]

while q:
    benefit, cost, state = heapq.heappop(q)
    benefit *= -1

    if state in visited:
        continue
    visited.add(state)

    if state == 'e':
        print("Part 2:", cost)
        break

    for rule in rules:
        p = re.compile(rule[1])
        indexes = [m.start() for m in p.finditer(state)]
        for i in indexes:
            new_state = state[:i] + rule[0] + state[i + len(rule[1]):]
            new_benefit = benefit + len(rule[1]) - len(rule[0])
            if new_state not in visited:
                heapq.heappush(q, (-new_benefit, cost + 1, new_state))
