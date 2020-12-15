import re

with open('input') as f:
    lines = [(x.strip()) for x in f]

def apply_bitmask(m: int, mask:str):
    res = []
    bin_value = bin(m)[2:].zfill(36)
    for i in range(len(mask)):
        if mask[i] in {'1', 'X'}:
            res.append(mask[i])
        elif mask[i] == '0':
            res.append(bin_value[i])
    return ''.join(res)

def realize(s : str):
    if s.count('X') == 0:
        return [s]
    res = []
    res += realize(s.replace('X', '0', 1), )
    res += realize(s.replace('X', '1', 1), )
    return res

inst = []
for line in lines:
    if line.startswith('mask'):
        inst.append(line[7:])
    else:
        li = line.split('=')
        val = int(li[1][1:])
        mem = re.search(r'\[(.*)\]', li[0]).groups()[0]
        mem = int(mem)
        inst.append((mem, val))

all_mem = {}
mask = None
for i in inst:
    if isinstance(i, str): # mask
        mask = i
        continue
    mem, val = i
    floating_bitmask = apply_bitmask(mem, mask)
    mem = realize(floating_bitmask)
    mem = [int(x, 2) for x in mem]
    for m in mem:
        all_mem[m] = val

print(sum(all_mem.values())) # part 2
