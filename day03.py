'''Advent of Code Day 3'''

# Part One
'''Needed hints and clues from message boards, started to
use the length  of Archimedes Spiral but got stuck'''

import math

n = 1024

# Find the layer by determining the closest odd square

layer = math.ceil(math.sqrt(n))

if layer % 2 != 0:
    pass
else:
    layer = layer + 1

# Radial distance
rdist = (layer - 1) / 2

# Find the shortest distance to path
path = []
for i in range(0, 4):
    path.append(layer**2 - ((layer - 1) * i) - math.floor(layer / 2))
pdist = []
for i in path:
    pdist.append(abs(i - n))
print(min(pdist) + rdist)
