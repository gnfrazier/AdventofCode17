'''Advent of Code Day 8'''

# Part One
instructions = []
registers = set()
reg_value = {}
comparisons = set()


def greater_than(cmd):
    if reg_value[cmd[4]] > int(cmd[6]):
        execute(cmd)


def less_than(cmd):
    if reg_value[cmd[4]] < int(cmd[6]):
        execute(cmd)


def greater_than_equal(cmd):
    if reg_value[cmd[4]] >= int(cmd[6]):
        execute(cmd)


def less_than_equal(cmd):
    if reg_value[cmd[4]] <= int(cmd[6]):
        execute(cmd)


def equal(cmd):
    if reg_value[cmd[4]] == int(cmd[6]):
        execute(cmd)


def not_equal(cmd):
    if reg_value[cmd[4]] != int(cmd[6]):
        execute(cmd)


def execute(task):
    old_value = reg_value[task[0]]
    if task[1] == 'inc':
        reg_value[task[0]] = old_value + int(task[2])

    elif task[1] == 'dec':
        reg_value[task[0]] = old_value - int(task[2])


check = {'>': greater_than,
         '<': less_than,
         '>=': greater_than_equal,
         '<=': less_than_equal,
         '==': equal,
         '!=': not_equal,
         }
with open('day08input.txt') as f:
    for line in f:
        components = line.strip('\n').split(' ')
        registers.add(components[0])
        comparisons.add(components[5])
        instructions.append(components)

for i in registers:
    reg_value[i] = 0
for i in instructions:
    # print(i)
    check[i[5]](i)
print(max(reg_value.values()))
