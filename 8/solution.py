# Part 2
with open('input') as f:
    lines = [x.strip().split() for x in f]
lines = [(x[0], int(x[1])) for x in lines]

def correct(lines):
    visited = set()
    accumulator = 0
    pos = 0
    while True:
        if pos in visited:
            return False # loops forever
        visited.add(pos)
        if pos == len(lines):
            return accumulator
        inst, val = lines[pos]
        if inst == 'acc':
            accumulator += val
            pos += 1
        elif inst == 'jmp':
            pos += val
        else:
            pos += 1

for pos in range(len(lines)):
    inst = lines[pos][0]
    temp = lines.copy()
    if inst == 'jmp':
        temp[pos] = ('nop', lines[pos][1])
    elif inst == 'nop':
        temp[pos] = ('jmp', lines[pos][1])
    else:
        continue
    c = correct(temp)
    if c:
        print(c)
