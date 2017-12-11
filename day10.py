'''Advent of Code Day 10'''

# Part One

lengths = [63, 144, 180, 149, 1, 255, 167,
           84, 125, 65, 188, 0, 2, 254, 229, 24]

input = []

for i in range(0, 256):
    input.append(i)

current_position = 0
skip_size = 0
last = len(input) - 1


for i in lengths:

    section = []
    read_position = current_position
    for step in range(i):

        section.append(input[read_position])
        read_position += 1
        if read_position > last:

            read_position = 0

    section.reverse()
    print(section)
    write_position = current_position

    for item in section:

        input[write_position] = item

        write_position += 1

        if write_position > last:
            write_position = 0

    '''Move the current position forward by that length plus the skip size.'''
    print(current_position, i, skip_size, last)
    if current_position + i + skip_size > last:
        current_position = current_position + i + skip_size - last - 1
    else:
        current_position = current_position + i + skip_size

    print(current_position, i, skip_size)

    skip_size += 1

    print(input, 'end')

print(input[0] * input[1])
