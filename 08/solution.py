with open('input.txt') as f:
    data = f.read()

import ast


total_1 = 0
total_2 = 0

for line in data.splitlines():

    total_1 += len(line)
    total_1 -= len(ast.literal_eval(line))

    total_2 += line.count("\"") + line.count("\\") + 2


print("Part 1:", total_1) # 1342
print("Part 2:", total_2) # 2074
