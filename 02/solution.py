with open('input.txt', 'r') as f:
    data = f.read()

def parse_line(line):
    l, w, h = line.split('x')
    return int(l), int(w), int(h)

def smallest_side_area(l, w, h):
    a1 = l * w
    a2 = l * h
    a3 = w * h
    return min(a1, a2, a3)

def total_surface_area(l, w, h):
    return 2 * ((l * w) + (l * h) + (w * h))

def shortest_perimiter(l, w, h):
    p1 = 2 * (l + w)
    p2 = 2 * (l + h)
    p3 = 2 * (w + h)
    return min(p1, p2, p3)

def volume(l, w, h):
    return l * w * h


total_paper_needed = 0
total_ribbon_needed = 0
for line in data.splitlines():
    l, w, h = parse_line(line)
    paper_needed = total_surface_area(l, w, h) + smallest_side_area(l, w, h)
    ribbon_needed = shortest_perimiter(l, w, h) + volume(l, w, h)
    total_paper_needed += paper_needed
    total_ribbon_needed += ribbon_needed

print("Part 1:", total_paper_needed)
print("Part 2:", total_ribbon_needed)
