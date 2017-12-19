
'''Advent of Code Day 17'''

# Part One
from collections import deque
step = 369
# step = 3 # Sample input
d = deque('0')


def insert(sd, rotation, new_value):

    sd.rotate(rotation)
    sd.appendleft(new_value)
    return sd


for i in range(1, 2018):
    d = insert(d, step, i)


print(d[-1])

# Part Two

step = 369
# step = 3 # Sample input
d = deque('0')


def insert(sd, rotation, new_value):

    sd.rotate(rotation)
    sd.appendleft(new_value)
    return sd


for i in range(1, 50000000):
    d = insert(d, step, i)


print(d[(d.index('0') - 1)])
