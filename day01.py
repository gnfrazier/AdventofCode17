'''Advent of Code - Day 1 2017'''

# Part 1

# Sample number
pin = '82317536746839978781792591955653325794933784832649781841433412843'
total = 0
# Use the last digit in the number sequence to start
previous = pin[-1:]

# Compare each digit to the previous one
for i in pin:
    if i == previous:
        # Add to total if they match
        total = total + int(i)

    previous = i

print(total)

# Part 2

total = 0
# Use the midpoint to start
length = int(len(pin))
span = int(length / 2)

# Compare each digit to the one halfway round
for i in pin:
    if i == pin[span]:
        # Add to total if they match
        total = total + int(i)

    span = span + 1
    # When at the end compare to the beginning
    if span == length:
        span = 0

print(total)
