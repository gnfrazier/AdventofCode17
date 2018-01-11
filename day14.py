'''Advent of Code Day 14'''
from collections import deque


def encrypt(raw):
    # From Day 10 Part Two
    suffix = [17, 31, 73, 47, 23]
    lengths = list(map(ord, raw))
    lengths = lengths + suffix
    input = []
    total_rotation = 0

    skip = 0
    for i in range(0, 256):
        input.append(i)
    input = deque(input)
    for r in range(64):
        for i in lengths:
            snip = []

            for r in range(i):
                snip.append(input.popleft())

            input.extendleft(snip)
            dist = i + skip
            input.rotate(-(dist))
            total_rotation += dist
            skip += 1
    input.rotate(total_rotation)

    dense = []
    while input:

        sparse = []
        for i in range(16):
            sparse.append(input.popleft())
        c = 0
        for b in sparse:
            c ^= b
        dense.append(c)
    end = []
    for d in dense:
        end.append(format(d, 'x').zfill(2))
    answer = ''.join(end)
    # print(answer)
    return answer


total = []
key = 'jzgqcdpd'
for i in range(128):
    raw = key + '-' + str(i)
    covered = encrypt(raw)
    hash = covered.encode('ascii')
    binary = bin(int(hash, 16))
    line = []
    for i in binary:
        line.append(i)

    total.append(sum(map(int, line[2:])))

print(sum(total))
