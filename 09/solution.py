from itertools import permutations

with open('input.txt') as f:
    data = f.read()

routes = {}

for line in data.splitlines():
    split = line.split()
    routes[frozenset([split[0], split[2]])] = int(split[-1])

all_destinations = set()
for route in routes:
    all_destinations.update(route)

possible_paths = list(permutations(all_destinations, len(all_destinations)))

costs = []
for path in possible_paths:
    cost = 0
    for i in range(len(path) - 1):
        cost += routes[frozenset([path[i], path[i+1]])]
    costs.append(cost)

print("Part 1:", min(costs))
print("Part 2:", max(costs))
