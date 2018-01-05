'''Advent of Code - Day 7 2017'''

# Part 2

children = []
parents = []
weight = {}
tower = {}
total_weight = {}
total_parts = {}


with open('day07input.txt') as f:
    for line in f:
        group = line.strip('\n').split('->')
        item = group[0].split(' (')
        key = item[0]
        value = item[1].strip(') ')
        weight[key] = int(value)

        if len(group) == 2:
            parent = group[0].split(' (')
            child = group[1].strip().split(', ')

            tower[key] = child


def check(single):
    balance = []
    for i in single:

        balance.append(total_weight[i])
    answer = (max(balance) == min(balance))
    return (answer)


def components(t):
    comp = set()
    try:
        for i in tower[t]:

            comp.add(i)
        return comp
    except:
        return comp


def all_comp():

    parts = set()
    for i in all_parts:
        parts.update(components(i))
    all_parts.update(parts)
    return len(all_parts)


def check_comp(t):
    total = []
    all_parts.add(t)
    b = len(all_parts)
    a = 0
    while b != a:
        b = len(all_parts)
        a = all_comp()
    for i in all_parts:
        total.append(weight[i])
    total_weight[t] = sum(total)
    total_parts[t] = all_parts
    return True


for t in weight:
    check_comp(t)
    all_parts = set()

bad_towers = {}
for i in tower:
    single = tower[i]
    good = check(single)
    if not good:
        bad_towers[i] = len(total_parts[i])
print('Out of balance towers:', bad_towers)


bad_names = list(bad_towers.keys())
bad_len = list(bad_towers.values())
highest = bad_names[bad_len.index(min(bad_len))]
print('Highest out of balance tower:', highest)


subs = {}
for i in tower[highest]:
    subs[i] = total_weight[i]
print('Weights of', highest, subs)


sk = list(subs.keys())
sv = list(subs.values())
heavy = sk[sv.index(max(sv))]
new = weight[heavy] - (max(sv) - min(sv))
print('Weight of ', heavy, 'is', weight[heavy])
print('New weight should be:', new)
