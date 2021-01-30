import collections

with open('input') as f:
    li = [x.strip() for x in f]

black_tiles = set()
alltiles = []
for p in li:
    new = p.replace('we', 'wxe') \
        .replace('ew', 'exw') \
        .replace('ee', 'exe') \
        .replace('ww', 'wxw')
    while p != new:
        p = new
        new = p.replace('we', 'wxe') \
            .replace('ew', 'exw') \
            .replace('ee', 'exe') \
            .replace('ww', 'wxw')

    if p[0] == 'e':
        p = 'x' + p
    elif p[0] == 'w':
        p = 'x' + p
    dirs = []
    for i in range(0, len(p), 2):
        dirs.append(p[i:i + 2])
    c = collections.Counter(dirs)
    c['ne'] -= c['sw']
    c['xe'] -= c['xw']
    c['se'] -= c['nw']
    c['xe'] += c['se']
    c['ne'] -= c['se']

    vals = (c['xe'], c['ne'])
    alltiles.append(vals)
    if vals in black_tiles:
        black_tiles.remove(vals)
    else:
        black_tiles.add(vals)

print('num black tiles', len(black_tiles)) # part 1

def num_adj_black_tiles(x, y, black_tiles):
    adj = [(x + 1, y), (x + 1, y - 1), (x, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1)]
    badj = [x in black_tiles for x in adj]
    return sum(badj)

#### part 2:
for _ in range(100):
    to_be_flipped = set()
    for b in black_tiles:  # flip black tiles
        x, y = b
        badj = num_adj_black_tiles(x, y, black_tiles)
        if badj not in {1, 2}:  # flip to white
            to_be_flipped.add(b)
    for b in black_tiles:  # flip white tiles
        x, y = b
        adj = [(x + 1, y), (x + 1, y - 1), (x, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1)]
        for neighbor in adj:
            if neighbor in black_tiles:
                continue
            # neighbor is white
            badj = num_adj_black_tiles(*neighbor, black_tiles)
            if badj == 2:
                to_be_flipped.add(neighbor)
    for tbf in to_be_flipped:
        if tbf in black_tiles:
            black_tiles.remove(tbf)
        else:
            black_tiles.add(tbf)

print(len(black_tiles))
