

from collections import deque
parts = []
with open('day24input.txt') as f:
    for line in f:
        each = line.strip('\n').split('/')

        parts.append(each)

dparts = deque(parts)

head = '0'
end = '0'
groups = {}
path = {}
tail = []
heads = []
dparts = deque(parts)
n = 0
path[n] = []
groups[n] = []
skip = None


def track(end, i):
    groups[n].append(i)
    path[n].append(end)
    if end == i[0]:
        path[n].append(i[1])
    if end == i[1]:
        path[n].append(i[0])
    return i


def mate(end, n, skip=None):
    global tail
    for i in dparts:
        # If the start of a new bridge, check that the head has not been used.
        if len(groups[n]) == 0:

            if i in heads:
                continue

        # Check if it is a tail prefer non-tails, or declare another end
        if i in tail:
            pass

        elif end in i:
            track(end, i)
            dparts.remove(i)
            return i

        else:
            pass

    return False


# Build out the set of bridges as groups
run = True
while run:
    found = mate(end, n, skip)
    try:
        end = path[n][-1]
    except:
        print('all tails found')
        run = False
        continue
    if found:
        pass
        # dparts.remove(found)
    else:  # reset dparts, increment n for next group
        dparts = deque(parts)

        if len(groups[n]) == 1:
            heads.append(groups[n][0])
            tail = []
        tail.append(groups[n][-1])
        n += 1
        end = head
        path[n] = []
        groups[n] = []

# Part One - find the strongest bridge
totals = []
for i in path:
    score = sum(map(int, path[i]))
    totals.append(score)
print('Strongest Bridge is', max(totals))

# Part Two - Find the longest bridge
length = []
for i in groups:
    length.append(len(groups[i]))
longest = length.index(max(length))
l = sum(map(int, path[longest]))
print('Longest Bridge is', l)
