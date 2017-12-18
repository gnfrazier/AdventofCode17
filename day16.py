from collections import deque

'''Advent of Code Day16'''

# Part One

# sample p = deque('abcde')
part_two = 'kbednhopmfcjilag'
# p = deque('abcdefghijklmnop')
pd = deque(part_two)

start = 'kbednhopmfcjilag'

# sample dance ='s1,x3/4,pe/b'
with open('day16input.txt') as f:
    dance = f.read()

steps = dance.split(',')


def spin(programs, X):
    programs.rotate(int(X))
    return programs


def exchange(programs, pair):
    M = pair.split('/')
    A = int(M[0])
    B = int(M[1])
    a = programs[A]
    b = programs[B]
    programs[B] = a
    programs[A] = b
    return programs


def partner(programs, pair):
    M = pair.split('/')
    A = M[0]
    B = M[1]

    a = int(programs.index(A))
    b = int(programs.index(B))
    programs[b] = A
    programs[a] = B
    return programs


guide = {'s': spin,
         'x': exchange,
         'p': partner,
         }
count = 0
for i in range(1000000000):
    for i in range(len(steps)):
        pd = guide[steps[i][0]](pd, steps[i][1:])
    end = ''.join(pd)
    # count+=1
    if end == start:
        print(count)
        break
    count += 1
end = ''.join(pd)
remainder = 1000000000 % count

pd = deque(part_two)
for i in range(remainder):
    for i in range(len(steps)):
        pd = guide[steps[i][0]](pd, steps[i][1:])
end = ''.join(pd)
print(end)
# not solved for part two
