with open('input') as f:
    lines = [x.strip() for x in f]

li = []
for s in lines:
    first = s[:7]
    bin = int(first.replace('F','0').replace('B','1'), 2)
    second = s[7:]
    bin2 = int(second.replace('L','0').replace('R','1'), 2)
    li.append((bin, bin2))

t = [x[0]*8 + x[1] for x in li]
print(max(t))

notin = []
for i in range(900):
    if i not in t:
        notin.append(i)
print(sorted(t))
print(notin) # visually inspect...