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

# Part Two

p = []
removed = []
with open('day20input.txt') as f:
    for line in f:
        row = line.replace('=<', ',').replace('>', ',').split(',')

        b = {'p': list(map(int, [row[1], row[2], row[3]])),
             'v': list(map(int, [row[6], row[7], row[8]])),
             'a': list(map(int, [row[11], row[12], row[13]])),
             'active': True}
        p.append(b)


def check():
    for i, v in enumerate(p):

        for c, u in enumerate(p):

            if i != c:
                if (p[i]['p'][0] == p[c]['p'][0])\
                        and (p[i]['p'][1] == p[c]['p'][1])\
                        and (p[i]['p'][2] == p[c]['p'][2]):

                    if p[i]['active']:
                        p[i]['active'] = False
                        removed.append(i)
                    if p[c]['active']:
                        p[c]['active'] = False
                        removed.append(c)
                    print('found one')


for z in range(100):

    for idx, v in enumerate(p[0]['p']):

        for i in p:

            i['v'][idx] = i['v'][idx] + i['a'][idx]

        for i in p:

            i['p'][idx] = i['p'][idx] + i['v'][idx]

        check()

active = []
for i in p:
    if i['active']:
        active.append(i)
print(len(active))
