'''Advent of Code Day 9'''

# Part One and Two

nest_level = 0
total_score = 0
garbage = False
garbage_count = 0

with open('day09input.txt') as f:
    # Read characters one at a time
    char = f.read(1)
    while char:
        # Check if in a garbage state
        if garbage:
            # Skip over the escaped characters
            if char == '!':
                f.read(1)
                char = f.read(1)
                continue
            elif char == '>':
                garbage = False  # Garbage close character
            else:
                # Count the garbage for part two
                garbage_count += 1
                char = f.read(1)
                continue

        # Track nest level
        if char == '{':
            nest_level += 1
            total_score += nest_level
        elif char == '}' and nest_level > 0:
            nest_level -= 1
        elif char == '<':
            garbage = True

        char = f.read(1)

print(total_score)
