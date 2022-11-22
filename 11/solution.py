import itertools


def next(s, level = 1):
    if s[-level] == 'z':
        return next(s, level + 1)
    else:
        return s[:-level] + chr(ord(s[-level])+1) + 'a'*(level-1)


def rule_1(s):
    for i in range(len(s)-2):
        if (
            ord(s[i+2]) - ord(s[i+1]) == 1 and
            ord(s[i+1]) - ord(s[i]) == 1
        ):
            return True
    return False


def rule_2(s):
    if (
        'i' in s or
        'o' in s or
        'l' in s
    ):
        return False
    return True


def rule_3(s):
    count = 0
    for _, g in itertools.groupby(s):
        if len(list(g)) > 1:
            count += 1
            if count == 2:
                return True
    return False


def valid_pw(s):
    return all([rule_1(s), rule_2(s), rule_3(s)])


def next_valid_pw(s):
    while True:
        s = next(s)
        if valid_pw(s):
            return s


input = "hxbxwxba"

part_1 = next_valid_pw(input)
print("Part 1:", part_1)

part_2 = next_valid_pw(part_1)
print("Part 2:", part_2)
