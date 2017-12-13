

'''Advent of Code Day 12'''

# Part One

'''input = ['0 <-> 2',
'1 <-> 1',
'2 <-> 0, 3, 4',
'3 <-> 2, 4',
'4 <-> 2, 3, 6',
'5 <-> 6',
'6 <-> 4, 5',
        ]'''
input = []
path_to_zero = {'0',}
groups = {}
programs = {}

with open('day12input.txt') as f:
    
    for line in f:
        line = str(line).replace('\n','')
        input.append(line)
        
for i, item in enumerate(input):
    
    input[i] =item.split(' <-> ')
    programs[input[i][0]] = input[i][1].split(', ')
    #input[i] =input[i].split(',')

for key in programs:
    groups[key]= set()
    

def search(pipe):
    if pipe in path_to_zero:
        path_to_zero.add(pipe)
    
    for key in programs:

        if programs[key].count(pipe) and key != pipe:
            groups[pipe].add(key)
            
        for item in programs[key]:
            if item in groups[pipe]:
                groups[pipe].add(key)
def recursion():
    for key in programs:
        search(key)
    for key in programs:
        search(key)
    for key in programs:
        search(key)
    for key in programs:
        search(key)
    
    
    

recursion()

print(len(groups['0']))