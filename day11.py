
'''Advent of Code Day 11'''

# Part One and Two


def move(start, step):
    x = start[0] + step[0]
    y = start[1] + step[1]
    z = start[2] + step[2]
    return (x, y, z)


def difference(a, b):
    return abs(a - b)


def distance(end=(0, 0, 0), start=(0, 0, 0)):
    calc = []
    calc.append((abs(start[0] - end[0])))
    calc.append((abs(start[1] - end[1])))
    calc.append((abs(start[2] - end[2])))
    dist = max(calc)
    return dist


heading = {'n': (-1, 1, 0),
           's': (1, -1, 0),
           'ne': (0, 1, -1),
           'se': (1, 0, -1),
           'sw': (0, -1, 1),
           'nw': (-1, 0, 1),
           }
farthest = []
with open('day11input.txt') as f:

    for line in f:
        breadcrumbs = line.strip('\n').split(',')

position = (0, 0, 0)
for crumb in breadcrumbs:
    position = move(position, heading[crumb])
    farthest.append(max(position))
    farthest.append(abs(min(position)))

print(distance(position))
print(max(farthest))
