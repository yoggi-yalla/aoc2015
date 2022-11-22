from itertools import product
import math


data1 = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""


raw_weapons, raw_armor, raw_rings = data1.split('\n\n')
raw_rings = raw_rings.replace(' +',  '')


def parse(s):
    out = []
    for line in s.splitlines()[1:]:
        split = line.split()
        out.append(
            (int(split[1]), int(split[2]), int(split[3]))
        )
    return out


weapons = parse(raw_weapons)
armor = parse(raw_armor)
rings = parse(raw_rings)

armor.append((0, 0, 0))
rings.append((0, 0, 0))

alternatives = list(product(weapons, armor, rings, rings))
alternatives = [a for a in alternatives if (a[2] != a[3]) or a[2] == (0,0,0)]

alternatives.sort(key = lambda a: sum(item[0] for item in a))


def get_stats(a):
    cost, dmg, arm = 0, 0, 0

    for i in range(4):
        cost += a[i][0]
        dmg += a[i][1]
        arm += a[i][2]
    
    return cost, dmg, arm


def fight(dmg, arm):
    effective_dmg = max(1, dmg - 2)
    effective_dmg_boss = max(1, 8 - arm)

    turns = math.ceil(100 / effective_dmg)
    turns_boss = math.ceil(100 / effective_dmg_boss)

    return 1 if turns <= turns_boss else 0


for a in alternatives:
    cost, dmg, arm = get_stats(a)
    if fight(dmg, arm):
        print("Part 1:", cost)
        break


for a in alternatives[::-1]:
    cost, dmg, arm = get_stats(a)
    if not fight(dmg, arm):
        print("Part 2:", cost)
        break
