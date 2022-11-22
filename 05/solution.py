with open('input.txt', 'r') as f:
    data = f.read()

illegal_strings = ['ab', 'cd', 'pq', 'xy']
vowels = 'aeiou'

def contains_three_vowels(s):
    return sum(s.count(ch) for ch in vowels) >= 3

def contains_doubles(s):
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            return True
    return False

def does_not_contain_illegal(s):
    if any(illegal in s for illegal in illegal_strings):
        return False
    return True

def is_nice(s):
    return all([
        contains_three_vowels(s),
        contains_doubles(s),
        does_not_contain_illegal(s)
    ])


nbr_nice_strings = sum(1 for s in data.splitlines() if is_nice(s))
print("Part 1:", nbr_nice_strings)


def new_rule_1(s):
    for i in range(len(s)-2):
        if s[i] + s[i+1] in s[i+2:]:
            return True
    return False

def new_rule_2(s):
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            return True
    return False

def is_nice_v2(s):
    return new_rule_1(s) and new_rule_2(s)


nbr_nice_strings_v2 = sum(1 for s in data.splitlines() if is_nice_v2(s))
print("Part 2:", nbr_nice_strings_v2)
