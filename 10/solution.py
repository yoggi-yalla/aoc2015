import itertools


def solve(input, n):
    for _ in range(n):
        output = ""
        for k, g in itertools.groupby(input):
            output += str(len(list(g))) + k
        input = output
    return len(output)


input = "1113122113"

print("Part 1:", solve(input, 40))
print("Part 2:", solve(input, 50))
