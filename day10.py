'''Advent of Code Day 10'''

# Part One

# l engths = [63,144,180,149,1,255,167,84,125,65,188,0,2,254,229,24]
lengths = [3, 4, 1, 5]
# Generate list 0 to 255
# input = []
input = [0, 1, 2, 3, 4, ]

current_position = 0
skip_size = 0
last = len(input) - 1
'''for i in range(0,256):
    input.append(i)'''

for i in lengths:
    # i = 3
    '''Reverse the order of that length of elements in the list,
    starting with the element at the current position.'''

    section = []
    read_position = current_position
    for step in range(i):
        print(current_position, read_position)
        section.append(input[read_position])
        read_position += 1
        if read_position >= last:

            read_position = 0
            print('wrap')
    section.reverse()
    print(section)
    write_position = current_position

    for item in section:
        # print(input, write_position, item)
        input[write_position] = item

        write_position += 1

        if write_position == (len(input) - 1):
            write_position = 0

    '''Move the current position forward by that length plus the skip size.'''
    if current_position + i + skip_size < last:
        current_position = current_position + i + skip_size
    else:
        current_position = current_position + i + skip_size - last

    '''Increase the skip size by one.'''
    skip_size = + 1
    # print(section)
    print(input, 'end')
    # print(current_position, skip_size)
