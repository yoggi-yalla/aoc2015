from collections import defaultdict

data = """33
14
18
20
45
35
16
35
1
13
18
13
50
44
48
6
24
41
30
42"""


containers = [int(s) for s in data.splitlines()]
results = defaultdict(int)


def nbr_of_solutions(remainder, containers, path=frozenset(), visited = set()):
    visited.add(path)

    if remainder == 0:
        results[len(path)] += 1
        return 1
    if remainder < 0:
        return 0

    solutions = []
    for i in range(len(containers)):
        if i in path:
            continue

        new_path = frozenset([*path, i])
        if new_path in visited:
            continue

        new_remainder = remainder - containers[i]
        solutions.append(nbr_of_solutions(new_remainder, containers, new_path))

    return sum(solutions)


print("Part 1:", nbr_of_solutions(150, containers))
print("Part 2:", sorted(results.items())[0][1])
