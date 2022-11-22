import numba

@numba.jit
def run(code, num):
    for _ in range(num):
        code *= 252533
        code %= 33554393
    return code


def triangular(n):
    return int(n * (n + 1) / 2)


row = 2978
col = 3083

num = row * (col - 1) + triangular(row - 1) + triangular(col - 1)
code = 20151125


print("Part 1 & 2:", run(code, num))
