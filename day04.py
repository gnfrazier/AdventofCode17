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

# Part Two

valid = []
pt1 = []
with open('day04input.txt') as f:
    for line in f:
        # Make a list of words in each passphrase
        words = line.strip('\n').split(' ')
        # Convert to a set to only have uniques
        unique = set(words)

        # Compare the lengths, add to pt1 list
        if len(words) == len(unique):
            pt1.append(words)

# Start with the valid list from Pt1
for phrase in pt1:
    flag = True
    sort = []

    for word in phrase:
        # alphabetize the letters in each word
        alphabetized = ''.join(sorted(word))
        # Append to a list
        sort.append(alphabetized)

    # Check if there is more than one of any word in the phrase
    for word in sort:
        if sort.count(word) > 1:
            flag = False

    if flag:
        valid.append(phrase)

print(len(valid))
