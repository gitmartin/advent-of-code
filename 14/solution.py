import re

with open('input') as f:
    lines = [(x.strip()) for x in f]

def masker(value, mask: str):
    bin_value = bin(value)[2:].zfill(36)
    res = []
    for i in range(len(mask)):
        if mask[i] == 'X':
            res.append(bin_value[i])
        else:
            res.append(mask[i])
    res = ''.join(res)
    return int(res, 2)

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
    all_mem[mem] = masker(val, mask)

print(sum(all_mem.values())) # part 1
