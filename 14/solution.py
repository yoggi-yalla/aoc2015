with open('input.txt') as f:
    data = f.read()


class Reindeer:
    def __init__(self, speed, endurance, rest):
        self.speed = speed
        self.endurance = endurance
        self.rest = rest

        self.distance = 0
        self.points = 0

        self.timer = 0
        self.state = 0


reindeers = []
for line in data.splitlines():
    split = line.split()

    speed = int(split[3])
    endurance = int(split[6])
    rest = int(split[-2])

    reindeers.append(Reindeer(speed, endurance, rest))


limit = 2503
for _ in range(limit):
    for r in reindeers:
        if r.state == 0:
            r.distance += r.speed

        r.timer += 1

        if r.state == 0 and r.timer >= r.endurance:
            r.timer = 0
            r.state = 1
        
        if r.state == 1 and r.timer >= r.rest:
            r.timer = 0
            r.state = 0
    
    current_leader = max(reindeers, key=lambda r: r.distance)
    current_leader.points += 1


print("Part 1:", max(reindeers, key=lambda r: r.distance).distance)
print("Part 2:", max(reindeers, key=lambda r: r.points).points)
