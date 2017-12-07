'''Advent of Code Day 6'''

# Part One

banks = [0, 2, 7, 0]
cycle = 0
prev_state = []


def string_value(int_list):
    sv = ''.join(list(map(str, banks)))

    return sv


def loop(start, distance, item):
    if (start + distance) > end:
        for i in range(start, end):
            item[i] = item[i] + 1

            print(item)
            distance = distance - 1
    else:
        for i in range(start, start + distance):
            print(start)
            item[i] = item[i] + 1

            print(item)
            distance = distance - 1
    return(0, distance, item)


prev_state = [string_value(banks), ]
current = None

while current not in prev_state:
    prev_state.append(current)

    end = len(banks)
    highest = max(banks)
    high_index = banks.index(highest)
    banks[high_index] = 0
    status = (high_index + 1, highest, banks)

    while status[1]:
        status = loop(status[0], status[1], status[2])

    current = string_value(banks)
    print(banks, 'end')
    cycle = cycle + 1

prev_state.append(current)

# Part Two

'''Solution for part two is the same code,
but use the output of part 1 as input.'''
