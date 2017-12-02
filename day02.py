'''Advent of Code Day 2'''

# Part One
rows = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]

checksum = 0
for line in rows:
    diff = max(line) - min(line)
    checksum = checksum + diff

print(checksum)

# Part Two

rows = [[5, 9, 2, 8],
        [9, 4, 7, 3],
        [3, 8, 6, 5]]

checksum = 0

for line in rows:
    eline = list(enumerate(line))

    for number in eline:
        denominator = number

        for numerator in eline:

            if numerator[0] != denominator[0]:

                if numerator[1] % denominator[1] == 0:
                    checksum = checksum + (numerator[1] / denominator[1])


print(checksum)
