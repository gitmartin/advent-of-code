with open('input') as f:
    lines = [(x.strip()) for x in f]

for i in range(len(lines)):
    lines[i] = list(lines[i])

num_rows = len(lines)
num_cols = len(lines[0])

def rule1(lines, r, c) -> bool:
    if lines[r][c] != 'L':
        return False
    if r > 0 and lines[r-1][c] == '#':
        return False
    if r < num_rows-1 and lines[r+1][c] == '#':
        return False
    if c > 0 and lines[r][c-1] == '#':
        return False
    if c < num_cols-1 and lines[r][c+1] == '#':
        return False
    # top left
    if r > 0 and c > 0 and lines[r-1][c-1] == '#':
        return False
    # top right
    if r > 0 and c < num_cols-1 and lines[r-1][c+1] == '#':
        return False
    # bottom left
    if r < num_rows-1 and c > 0 and lines[r+1][c-1] == '#':
        return False
    # bottom right
    if r < num_rows-1 and c < num_cols-1 and lines[r+1][c+1] == '#':
        return False
    return True

def rule2(lines, r, c) -> bool:
    if lines[r][c] != '#':
        return False
    num_occ = 0
    if r > 0 and lines[r-1][c] == '#':
        num_occ += 1
    if r < num_rows-1 and lines[r+1][c] == '#':
        num_occ += 1
    if c > 0 and lines[r][c-1] == '#':
        num_occ += 1
    if c < num_cols-1 and lines[r][c+1] == '#':
        num_occ += 1
    # top left
    if r > 0 and c > 0 and lines[r-1][c-1] == '#':
        num_occ += 1
    # top right
    if r > 0 and c < num_cols-1 and lines[r-1][c+1] == '#':
        num_occ += 1
    # bottom left
    if r < num_rows-1 and c > 0 and lines[r+1][c-1] == '#':
        num_occ += 1
    # bottom right
    if r < num_rows-1 and c < num_cols-1 and lines[r+1][c+1] == '#':
        num_occ += 1
    if num_occ >= 4:
        return True
    return False

while True:
    new_vals = {}
    for r in range(num_rows):
        for c in range(num_cols):
            if rule1(lines,r,c):
                new_vals.update({(r,c): '#'})
            elif rule2(lines,r,c):
                new_vals.update({(r, c): 'L'})
    if not new_vals:
        break
    for nv in new_vals:
        r, c = nv[0], nv[1]
        lines[r][c] = new_vals[nv]

occ = 0
for row in lines:
    for seat in row:
        if seat == '#':
            occ += 1
print(occ) # part 1