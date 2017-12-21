
dgram = {}
row = 0
with open('day19input.txt') as f:
    for line in f:
        dgram[row] = line.strip('\n')
        row += 1
d = {0: 'd', }
crumb = [0, ]


def down(x, y):
    if dgram[y][x] == '|':
        return (x, y + 1)
    elif dgram[y][x] == '+':
        print('turn')
        try:
            if dgram[y][x + 1] != ' ':
                print('right')
                d[0] = 'r'
                return (x + 1, y)
        except:
            print('edge')
        try:
            if dgram[y][x - 1] != ' ':
                print('left')
                d[0] = 'l'
                return (x - 1, y)
        except:
            print('edge')
    else:
        crumb.append(dgram[y][x])
        return (x, y + 1)


def up(x, y):
    if dgram[y][x] == '|':
        return (x, y - 1)
    elif dgram[y][x] == '+':
        try:
            if dgram[y][x + 1] != ' ':
                d[0] = 'r'
                return (x + 1, y)
        except:
            print('edge')
        try:
            if dgram[y][x - 1] != ' ':
                d[0] = 'l'
                return (x - 1, y)
        except:
            print('edge')
    else:
        crumb.append(dgram[y][x])
        return (x, y - 1)


def right(x, y):
    if dgram[y][x] == '-':
        return (x + 1, y)
    elif dgram[y][x] == '+':
        try:
            if dgram[y - 1][x] != ' ':
                d[0] = 'u'
                return (x, y - 1)
        except:
            print('edge')
        try:
            if dgram[y + 1][x] != ' ':
                d[0] = 'd'
                return (x, y + 1)
        except:
            print('edge')
    else:
        crumb.append(dgram[y][x])
        return (x + 1, y)


def left(x, y):
    if dgram[y][x] == '-':
        return (x - 1, y)
    elif dgram[y][x] == '+':
        try:
            if dgram[y - 1][x] != ' ':
                d[0] = 'u'
                return (x, y - 1)
        except:
            print('edge')
        try:
            if dgram[y + 1][x] != ' ':
                d[0] = 'd'
                return (x, y + 1)
        except:
            print('edge')
    else:
        crumb.append(dgram[y][x])
        return (x - 1, y)


# Find the start block
b = (dgram[0].index('|'), 0)

menu = {'d': down,
        'u': up,
        'l': left,
        'r': right,
        }

while dgram[b[1]][b[0]] != 'S':
    b = menu[d[0]](b[0], b[1])
    print(b, d)

crumb.append(dgram[b[1]][b[0]])
end = []
for i in crumb[1:]:
    if (i != '-') and (i != '|'):
        end.append(i)
output = ''.join(end)
output
