import itertools
import math

with open('input.txt') as f:
    data = f.read()


def get_next_combo(weights, target):
    for i in range(len(weights)):
        output = []
        for combo in itertools.combinations(weights, i):
            if sum(combo) == target:
                output.append(set(combo))
        output.sort(key=lambda v: math.prod(v))
        yield from output


def valid_combo(combo, weights, target):
    subset = weights - combo

    if sum(subset) == target:
        return True

    for subcombo in get_next_combo(subset, target):
        if valid_combo(subcombo, subset, target):
            return True

    return False 


weights = set([int(x) for x in data.splitlines()])

target_1 = sum(weights) / 3
target_2 = sum(weights) / 4


for combo in get_next_combo(weights, target_1):
    if valid_combo(combo, weights, target_1):
        print("Part 1:", math.prod(combo))
        break
        
for combo in get_next_combo(weights, target_2):
    if valid_combo(combo, weights, target_2,):
        print("Part 2:", math.prod(combo))
        break
