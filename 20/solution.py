from sympy import divisors


goal = 36000000


def presents(n):
    return sum(
        10 * d for d in divisors(n)
    )


def presents_2(n):
    return sum(
        11 * d for d in divisors(n)
        if d * 50 >= n
    )


def run(goal, p_func):
    i = 0
    while True:
        p = p_func(i)
        if p >= goal:
            return i
        i+=1


print("Part 1:", run(goal, presents))
print("Part 2:", run(goal, presents_2))
