with open('input.txt') as f:
    data = f.read()


grid = [[ch for ch in line] for line in data.splitlines()]
dims = len(grid), len(grid[0])


def in_grid(dims, i, j):
    return all((
        i >= 0,
        i < dims[0],
        j >= 0,
        j < dims[1]
    ))


def neighbors(grid, i, j):
    return (
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),

        (i, j - 1),
        (i, j + 1),

        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
    )


def update_grid(grid, buffer):
    for (i,j), v in buffer.items():
        grid[i][j] = v


def fill_buffer(grid):
    buffer = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            sum = 0
            for ii, jj in neighbors(grid, i, j):
                if in_grid(dims, ii, jj):
                    if grid[ii][jj] == '#':
                        sum += 1
            
            if grid[i][j] == '#':
                if sum not in (2, 3):
                    buffer[i,j] = '.'
            
            if grid[i][j] == '.':
                if sum == 3:
                    buffer[i,j] = '#'
    return buffer


def run(grid, part_2):
    for _ in range(100):
        buffer = fill_buffer(grid)
        if part_2:
            buffer[0,0] = '#'
            buffer[0,-1] = '#'
            buffer[-1,0] = '#'
            buffer[-1,-1] = '#'

        update_grid(grid, buffer)

    return count(grid)


def count(grid):
    return sum(line.count('#') for line in grid)


grid_2 = [[ch for ch in line] for line in grid]

print("Part 1:", run(grid, False))
print("Part 2:", run(grid_2, True))
