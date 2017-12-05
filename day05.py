'''Advent of Code Day 5'''

# Part One
start = []
# Read the txt file, append one line per item
with open('day05input.txt') as f:
    for line in f:
        data = int(line.strip('\n'))
        start.append(data)

# Enumerate the list
inst = list(enumerate(start))
# Determine the number of the last entry
last = inst[-1]
escape = last[0]


# Increase the jump by one
def cycle(pair):
    offset = (pair[0], pair[1] + 1)
    return offset


cycles = 0
current = 0

# Run through the instructions, increase after an instruction has been used.
# If the jump is beyond the last value then escape.
while current <= escape:
    jump = inst[current]
    next_step = current + jump[1]
    inst[current] = cycle(jump)

    current = next_step
    cycles = cycles + 1
print(inst)
print(escape, current, cycles)

# Part Two
# Same as part 1 with an added if to increase or decrease

inst = list(enumerate(start))
last = inst[-1]
escape = last[0]


def cycle(pair):
    '''Added conditional for increase or decrease for part two'''
    if pair[1] >= 3:
        offset = (pair[0], pair[1] - 1)
    else:
        offset = (pair[0], pair[1] + 1)
    return offset


cycles = 0
current = 0
while current <= escape:
    jump = inst[current]
    next_step = current + jump[1]
    inst[current] = cycle(jump)
    current = next_step
    cycles = cycles + 1

print(cycles)
