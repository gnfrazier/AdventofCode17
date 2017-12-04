'''Advent of Code Day 4'''

# Part One

valid = []
with open('day04input.txt') as f:

    for line in f:
        # Make a list of words in each passphrase
        words = line.strip('\n').split(' ')
        # Convert to set to only have uniques
        unique = set(words)

        # Compare the lengths, add to valid list
        if len(words) == len(unique):
            valid.append(words)

print(len(valid))
