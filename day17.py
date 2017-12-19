
'''Advent of Code Day 17'''


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
