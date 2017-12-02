'''Advent of Code Day 2'''

# Part One
rows = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]

checksum = 0
for line in rows:
    # Find the difference largest and smallest value in a line
    diff = max(line) - min(line)
    # Add that difference to the total
    checksum = checksum + diff

print(checksum)

# Part Two

rows = [[5, 9, 2, 8],
        [9, 4, 7, 3],
        [3, 8, 6, 5]]

checksum = 0

for line in rows:
    # Enumerate the numbers on a line
    eline = list(enumerate(line))

    # Iterate through the numbers as denominators
    for number in eline:

        denominator = number

        for numerator in eline:
            # Don't divide by the same position number
            if numerator[0] != denominator[0]:
                # Check the modulo, if zero then add quotient to total
                if numerator[1] % denominator[1] == 0:
                    checksum = checksum + (numerator[1] / denominator[1])


print(checksum)
