
last_played = 0
run = True


def snd(reg, value):
    global last_played
    last_played = str(registers[reg])

    return 1


def _set(reg, value):
    registers[reg] = value

    return 1


def add(reg, value):
    registers[reg] = registers[reg] + value

    return 1


def multiply(reg, value):
    registers[reg] = registers[reg] * value

    return 1


def modulo(reg, value):
    registers[reg] = registers[reg] % value

    return 1


def recover(reg, value):
    if registers[reg] != 0:
        print('playing: ', last_played)
        global run
        run = False
    return 1


def jump(reg, value):
    if registers[reg] != 0:
        return int(value)
    else:
        return 1


# Patch to account for str vs int in value position
def glue(inst):
    try:
        inc = menu[inst[0]](inst[1], int(inst[2]))
    except:
        val = registers[inst[2]]
        inc = menu[inst[0]](inst[1], val)
    return inc


with open('day18input.txt') as f:
    raw = f.read()
    inst = raw.split('\n')
instructions = {}
registers = {}
# Set registers to 0
# Set instructions
# Strip the reg refrence out it duplicated

for i, v in enumerate(inst):
    registers[v[4]] = 0
    instructions[i] = [v[:3], v[4], v[4:]]
    if len(instructions[i][2]) > 1:
        instructions[i][2] = instructions[i][2].strip(instructions[i][1] + ' ')

# TODO this is a patch to correct for when the dup is valid
instructions[3][2] = 'p'

# Lookup the instructions
menu = {'snd': snd,
        'set': _set,
        'add': add,
        'mul': multiply,
        'mod': modulo,
        'rcv': recover,
        'jgz': jump,
        }

# Position to start
pos = 0

# Run flag set to false by condition in the problem
while run:
    pos += glue(instructions[pos])
