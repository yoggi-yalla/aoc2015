import numpy as np
import re

pattern = re.compile(r"\w+: \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+)")

with open('input.txt') as f:
    data = f.read()


def parse_line(line):
    return np.array(re.match(pattern, line).groups(), dtype=int)

ingredients = np.array([parse_line(l) for l in data.splitlines()]).T


def cost(weights, ingredients):
    s = np.sum(weights * ingredients[:4,:], axis=1)
    s[s < 0] = 0
    return np.prod(s)


def calories(weights, ingredients):
    return np.sum(weights * ingredients[-1, :])


max_cost_1 = 0
max_cost_2 = 0
for i in range(1, 101):
    for j in range(1, 101-i):
        for k in range(1, 101-i-j):
            l = 100 - i - j - k
            weights = np.array([i,j,k,l])
            this_cost = cost(weights, ingredients)
            max_cost_1 = max(this_cost, max_cost_1)
            if calories(weights, ingredients) == 500:
                max_cost_2 = max(this_cost, max_cost_2)


print("Part 1:", max_cost_1)
print("Part 2:", max_cost_2)

for e in ingredients:
    print(e)
