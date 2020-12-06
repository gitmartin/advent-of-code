# Part 2
groups = []
with open('input') as f:
    g = []
    for line in f:
        line = line.strip()
        if line == '':
            groups.append(g)
            g = []
        else:
            g.append(line)
    groups.append(g)

count = 0
for people in groups:
    count += len(set.intersection(*[set(x) for x in people]))
print(count)