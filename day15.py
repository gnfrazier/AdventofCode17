'''Day15'''

factor = {'a': 16807,
         'b': 48271,
         }
divisor = 2147483647

match_count = 0

def gen(name, value):
    result = (factor[name] * value) % divisor
    
    return result

def judge(a,b):
    # print(a,b)
    if bin(a)[-16:]==bin(b)[-16:]:
        return 1
    else:
        return 0
    
value_a = 722
value_b = 354


for i in range(40000000):
    value_a = gen('a',value_a)
    value_b = gen('b',value_b)
    match_count+=judge(value_a,value_b)
    # print()
match_count