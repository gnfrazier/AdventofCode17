'''Advent of Code Day 10'''
from collections import deque
# Part One

lengths = [63,144,180,149,1,255,167,84,125,65,188,0,2,254,229,24]
#lengths = [3, 4, 1, 5]
input = []
#input = [0, 1, 2, 3, 4,]
total_rotation = 0

skip = 0
for i in range(0,256):
    input.append(i)
input = deque(input)

for i in lengths:
    snip = []

    for r in range(i):    
        snip.append(input.popleft())

    input.extendleft(snip)
    dist = i+skip
    input.rotate(-(dist))
    total_rotation+=dist
    skip+=1
input.rotate(total_rotation)
a = input.popleft()
b = input.popleft()
print(a*b)