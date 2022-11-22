import re

PATTERN = re.compile(r'.* (\d+),(\d+) through (\d+),(\d+)')

with open('input.txt', 'r') as f:
    data = f.read()


def extract_numbers(line):
    x1, y1, x2, y2 = re.match(PATTERN, line).groups()
    return int(x1), int(y1), int(x2), int(y2)


def count_grid(grid):
    counter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            counter += grid[row][col]
    return counter


def part_1():
    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in data.splitlines():
        x1, y1, x2, y2 = extract_numbers(line)

        for row in range(x1, x2 + 1):
            for col in range(y1, y2 +1):
                if line.startswith('turn on'):
                    grid[row][col] = 1
                elif line.startswith('turn off'):
                    grid[row][col] = 0
                else:
                    grid[row][col] ^= 1 
    
    return count_grid(grid)



def part_2():
    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in data.splitlines():
        x1, y1, x2, y2 = extract_numbers(line)

        for row in range(x1, x2 + 1):
            for col in range(y1, y2 +1):
                if line.startswith('turn on'):
                    grid[row][col] += 1
                elif line.startswith('turn off'):
                    grid[row][col] -= 1
                    grid[row][col] = max(grid[row][col], 0)
                else:
                    grid[row][col] += 2
    
    return count_grid(grid)


print("Part 1:", part_1()) # 377891
print("Part 2:", part_2()) # 14110788
