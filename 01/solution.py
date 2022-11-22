with open ('input.txt', 'r') as f:
    data = f.read()

level = 0
for ch in data:
    if ch == '(':
        level += 1
    else:
        level -= 1
print("Part 1:", level)


level = 0
for i, ch in enumerate(data):
    if ch == '(':
        level += 1
    else:
        level -= 1
        if level < 0:
            print("Part 2:", i + 1)
            break
