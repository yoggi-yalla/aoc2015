import heapq

BOSS_DMG = 9
BOSS_HP = 51

START_STATE = (0, BOSS_HP, 50, 500, 0, 0, 0)

def next_states(state, hard=True):
    cost, boss_hp, hp, mana, t1, t2, t3 = state

    if hard:
        hp -= 1

    if hp <= 0:
        return []

    if t2 >= 1:
        boss_hp -= 3

    if boss_hp <= 0:
        return [(cost, boss_hp, hp, mana, 0, 0, 0)]
    
    if t3 >= 1:
        mana += 101

    t1 = max(0, t1-1)
    t2 = max(0, t2-1)
    t3 = max(0, t3-1)

    moves = []
    if mana < 53:
        return []
    if mana >= 53:
        moves.append((cost+53, boss_hp-4, hp, mana-53, t1, t2, t3))
    if mana >= 73:
        moves.append((cost+73, boss_hp-2, hp+2, mana-53, t1, t2, t3))
    if mana >= 113 and t1 <= 0:
        moves.append((cost+113, boss_hp, hp, mana-113, 6, t2, t3))
    if mana >= 173 and t2 <= 0:
        moves.append((cost+173, boss_hp, hp, mana-173, t1, 6, t3))
    if mana >= 229 and t3 <= 0:
        moves.append((cost+229, boss_hp, hp, mana-229, t1, t2, 5))

    states = []
    for m in moves:
        cost, boss_hp, hp, mana, t1, t2, t3 = m
        
        if t2 >= 1:
            boss_hp -= 3
        
        if boss_hp <= 0:
            return[(cost, boss_hp, hp, mana, max(0, t1-1), max(0, t2-1), max(0, t3-1))]

        if t1 >= 1:
            hp -= max(1, (BOSS_DMG - 7))
        else:
            hp -= BOSS_DMG

        if hp <= 0:
            continue

        if t3 >= 1:
            mana += 101

        t1 = max(0, t1-1)
        t2 = max(0, t2-1)
        t3 = max(0, t3-1)

        states.append((cost, boss_hp, hp, mana, t1, t2, t3))
    
    return states


def run(hard_mode: bool):
    visited = set()
    q = [START_STATE]
    while q:
        state = heapq.heappop(q)

        if state in visited:
            continue
        visited.add(state)

        cost, boss_hp = state[:2]
        if boss_hp <= 0:
            return cost
        
        for s in next_states(state, hard_mode):
            if s not in visited:
                heapq.heappush(q, s)


print("Part 1:", run(False))
print("Part 2:", run(True))
