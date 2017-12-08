'''Advent of Code Day 7'''

# Part One
children = []
parents = []
with open('day07input.txt') as f:
    for line in f:
        # split out the children
        group = line.strip('\n').split('->')
        # if the line had a child group, add kids to children
        if len(group) == 2:
            child = group[1].strip().split(', ')

            for i in child:
                children.append(i)
        # make a list of parents
        parent = group[0].split(' (')
        parents.append(parent[0])

# Find the parent that is not in children
for parent in parents:
    if parent not in children:
        print(parent)
