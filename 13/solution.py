import itertools

with open('input.txt') as f:
    data = f.read()


scores = {} # {(name1, name2): score}
all_names = set()

for line in data.splitlines():
    split = line.split()
    name1, name2 = split[0], split[-1][:-1]
    score = int(split[3]) if split[2] == 'gain' else -int(split[3])

    scores[name1, name2] = score
    all_names.update([name1, name2])


def best_score(all_names, scores):
    possible_arrangements = itertools.permutations(all_names)

    highest_score = 0
    for arr in possible_arrangements:
        score = 0
        for i in range(len(all_names) - 1):
            score += scores[arr[i], arr[i+1]]
            score += scores[arr[i+1], arr[i]]
        score += scores[arr[0], arr[-1]]
        score += scores[arr[-1], arr[0]]

        highest_score = max(score, highest_score)
    
    return highest_score


print("Part 1:", best_score(all_names, scores))

for n in all_names:
    scores[n, "me"] = 0
    scores["me", n] = 0

all_names.add("me")

print("Part 2:", best_score(all_names, scores))
