'''Advent of Code Day 20'''

# Part One

p = []
final = []
with open('day20input.txt') as f:
    for line in f:
        row = line.replace('=<', ',').replace('>', ',').split(',')

        b = {'p': list(map(int, [row[1], row[2], row[3]])),
             'v': list(map(int, [row[6], row[7], row[8]])),
             'a': list(map(int, [row[11], row[12], row[13]]))}
        p.append(b)
for i in p:
    final.append(sum(map(abs, i['a'])))


print(final.index(min(final)))
