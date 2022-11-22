# This solution assumes that out of all sets that are in the group with shortest length, 
# The one with the smallest QE is a valid way to make the first cut and still be left
# with a subset that can be evenly divided into the remaining compartments. 

# There is no guarantee that this works but it works for my puzzle input.


import itertools
import math

with open('input.txt') as f:
    data = f.read()


def get_next_qe(weights, target):
    for i in range(len(weights)):
        output = []
        for combo in itertools.combinations(weights, i):
            if sum(combo) == target:
                output.append(set(combo))
        output = sorted(map(math.prod, output))
        yield from output


weights = set([int(x) for x in data.splitlines()])

target_1 = sum(weights) / 3
target_2 = sum(weights) / 4

print("Part 1:", next(get_next_qe(weights, target_1)))
print("Part 2:", next(get_next_qe(weights, target_2)))
