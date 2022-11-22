with open('input.txt', 'r') as f:
    data = f.read()


from collections import deque

instructions = deque([x.split() for x in data.splitlines()])


def run_instructions(instructions):
    memory = {}

    while instructions:
        instruction = instructions.popleft()
        
        if 'AND' in instruction:
            v1, v2, dest = instruction[0], instruction[2], instruction[-1]
            if v1 in memory and v2 in memory:
                memory[dest] = memory[v1] & memory[v2]
            elif v1 == '1' and v2 in memory:
                memory[dest] = int(v1) & memory[v2]
            else:
                instructions.append(instruction)

        elif 'OR' in instruction:
            v1, v2, dest = instruction[0], instruction[2], instruction[-1]
            if v1 in memory and v2 in memory:
                memory[dest] = memory[v1] | memory[v2]
            else:
                instructions.append(instruction)
        
        elif 'LSHIFT' in instruction:
            v1, v2, dest = instruction[0], instruction[2], instruction[-1]
            if v1 in memory:
                memory[dest] = memory[v1] << int(v2)
            else:
                instructions.append(instruction)

        elif 'RSHIFT' in instruction:
            v1, v2, dest = instruction[0], instruction[2], instruction[-1]
            if v1 in memory:
                memory[dest] = memory[v1] >> int(v2)
            else:
                instructions.append(instruction)
            
        elif 'NOT' in instruction:
            v, dest = instruction[1], instruction[-1]
            if v in memory:
                memory[dest] = memory[v] ^ 0b1111111111111111
            else:
                instructions.append(instruction)
        
        else:
            v, dest = instruction[0], instruction[-1]
            if v in memory:
                memory[dest] = memory[v]
            else:
                try:
                    memory[dest] = int(v)
                except:
                    instructions.append(instruction)
        
    return memory


memory = run_instructions(instructions.copy())
part_1 = memory['a']


for i, instruction in enumerate(instructions):
    if instruction[-1] == 'b':
        instructions[i] = [memory['a'], '->', 'b']


memory = run_instructions(instructions.copy())
part_2 = memory['a']


print("Part 1:", part_1) # 16076
print("Part 2:", part_2) # 2797
