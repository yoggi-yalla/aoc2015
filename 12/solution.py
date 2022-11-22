import json
from queue import Queue

with open('input.txt') as f:
    tree = json.load(f)


def count(tree, skip_red):
    q = Queue()

    for e in tree:
        q.put(e)

    tot = 0
    while not q.empty():
        e = q.get()
        if type(e) == list:
            for ee in e:
                q.put(ee)
        elif type(e) == dict:
            if "red" in e.values() and skip_red == True:
                continue
            for ee in e.values():
                q.put(ee)
        elif type(e) == int:
            tot += e
        else:
            continue

    return tot

print("Part 1:", count(tree, False))
print("Part 2:", count(tree, True))
