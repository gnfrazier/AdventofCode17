
last_played = 0
run = True
mulcount = []


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


def sub(reg, value):
    registers[reg] = registers[reg] - value
    return 1


def multiply(reg, value):
    registers[reg] = registers[reg] * value
    mulcount.append(1)
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


def jz(reg, value):
    if reg.isalpha():
        x = registers[reg]
    else:
        x = int(reg)
    if x != 0:
        return int(value)
    else:
        return 1


def glue(inst):
    # print('glued', inst)
    try:
        inc = menu[inst[0]](inst[1], int(inst[2]))
    except:
        val = registers[inst[2]]
        inc = menu[inst[0]](inst[1], val)
    return inc


with open('day23input.txt') as f:
    raw = f.read()
    inst = raw.split('\n')
instructions = {}
registers = {}
# Set registers to 0
for i, v in enumerate(inst):
    registers[v[4]] = 0
    instructions[i] = [v[:3], v[4], v[4:]]
    if len(instructions[i][2]) > 1:
        instructions[i][2] = instructions[i][2].strip(instructions[i][1] + ' ')


menu = {'snd': snd,
        'set': _set,
        'add': add,
        'sub': sub,
        'mul': multiply,
        'mod': modulo,
        'rcv': recover,
        'jgz': jump,
        'jnz': jz,
        }


pos = 0
pos += glue(instructions[pos])
while run:
    pos += glue(instructions[pos])
    if pos < 0:
        run = False
    if pos >= 32:
        run = False

print(sum(mulcount))
