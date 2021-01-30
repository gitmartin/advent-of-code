# Part 2
inp = 916438275

cups = list(map(int, list(str(inp))))
cups = cups + list(range(10, 1_000_000+1))

N = len(cups)
lo = min(cups)
hi = max(cups)
cd = {}

for c in range(len(cups)-1):
    cd[cups[c]] = cups[c+1]
cd[cups[-1]] = cups[0]

curr_cup = cups[0]
for m in range(10_000_000):
    c1 = cd[curr_cup]
    c2 = cd[c1]
    c3 = cd[c2]
    temp = cd[c3]
    dest_cup = curr_cup - 1
    if dest_cup < lo:
        dest_cup = hi
    while dest_cup in {c1, c2, c3} or dest_cup < lo:
        if dest_cup < lo:
            dest_cup = hi
            continue
        dest_cup -= 1
    cd[curr_cup] = temp
    cd[c3] = cd[dest_cup]
    cd[dest_cup] = c1
    curr_cup = temp

a = cd[1]
b = cd[a]
print(int(a)*int(b))
