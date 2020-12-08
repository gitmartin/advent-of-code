import re
with open('input') as f:
    lines = [x.strip() for x in f]

nodes = {}
for line in lines:
    line = line.replace('.', '').replace(',', '')
    line = re.split('bags contain|bags|bag', line)
    line = [x.strip() for x in line if x]
    color = line[0]
    adj = line[1:] # adjacent
    adj = [x.replace('no other', '0 no other') for x in adj]
    adj = [(x[2:], int(x[0])) for x in adj]
    nodes[color] = set(adj)

def sg_in_subnodes(node):
    if node == 'shiny gold':
        return True
    cols = {x[0] for x in nodes[node] if x[0] != 'no other'}
    return any([sg_in_subnodes(n) for n in cols])

def num_bags(node_tuple):
    if node_tuple[0] == 'no other':
        return 0
    return node_tuple[1] * (1 + sum(num_bags(n) for n in nodes[node_tuple[0]]))

count = 0
for n in nodes:
    # check if n can contain a shiny gold bag
    if n == 'shiny gold':
        cols = {x[0] for x in nodes[n] if x[0] != 'no other'}
        count += sum(sg_in_subnodes(x) for x in cols)
    else:
        if sg_in_subnodes(n):
            count += 1

print('count:', count)
print('numbags:', num_bags(('shiny gold', 1)) - 1)
