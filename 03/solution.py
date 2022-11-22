import collections

with open('input.txt', 'r') as f:
    data = f.read()


def get_new_pos(pos, ch):
    if ch == '^':
        return (pos[0] + 1, pos[1])
    elif ch == 'v':
        return (pos[0] - 1, pos[1])
    elif ch == '>':
        return (pos[0], pos[1] + 1)
    elif ch == '<':
        return (pos[0], pos[1] - 1)
    else:
        raise ValueError('invalid direction')


def part_1():
    received_presents = collections.defaultdict(int)

    santa_pos = (0, 0)

    for ch in data:
        santa_pos = get_new_pos(santa_pos, ch)
        received_presents[santa_pos] += 1
    
    return len(received_presents)


def part_2():
    received_presents = collections.defaultdict(int)

    santa_pos = (0, 0)
    robo_santa_pos = (0, 0)

    for ch in data[::2]:
        santa_pos = get_new_pos(santa_pos, ch)
        received_presents[santa_pos] += 1

    for ch in data[1::2]:
        robo_santa_pos = get_new_pos(robo_santa_pos, ch)
        received_presents[robo_santa_pos] += 1
    
    return len(received_presents)


print("Part 1:", part_1()) # 2572
print("Part 2:", part_2()) # 2631
