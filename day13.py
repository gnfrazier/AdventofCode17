
'''Advent of Code Day 13'''

# Part One
'''Sample Input
input = {0: 3,
        1: 2,
        4: 4,
        6: 4,
            }'''

input = {}
with open('day13input.txt') as f:

    for line in f:
        line = str(line).replace('\n', '')
        s = line.split(': ')
        input[int(s[0])] = int(s[1])


scan = {}
dist = 0
for i in range(2, 20):
    scan[i] = i + dist
    dist += 1

severity = 0
for key in input:
    if key % scan[input[key]] == 0:
        severity += (key * input[key])
print(severity)

# Part Two
#%%writefile day13.py

'''Advent of Code Day 13'''

# Part two

# Sample Input
'''input = {0: 3,
        1: 2,
        4: 4,
        6: 4,
            }'''

input = {}
with open('day13input.txt') as f:

    for line in f:
        line = str(line).replace('\n', '')
        s = line.split(': ')
        input[int(s[0])] = int(s[1])
scan = {}
dist = 0
for i in range(2, 20):
    scan[i] = i + dist
    dist += 1

delay = -1
severity = 1
while severity:
    delay += 1
    d_input = {}
    for item in input:
        k = item + delay
        d_input[k] = input[item]

    severity = 0
    for key in d_input:
        if key % scan[d_input[key]] == 0:
            severity += (key * d_input[key])


print(severity, delay)
d_input
