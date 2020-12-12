with open('input') as f:
    lines = [(x.strip()) for x in f]

for i in range(len(lines)):
    lines[i] = list(lines[i])

num_rows = len(lines)
num_cols = len(lines[0])

def up(lines, r, c):
    if r == 0:
        return None
    while r > 0:
        r -= 1
        if lines[r][c] != '.':
            return (r, c)
    return None

def down(lines, r, c):
    if r == num_rows-1:
        return None
    while r < num_rows-1:
        r += 1
        if lines[r][c] != '.':
            return (r, c)
    return None

def left(lines, r, c):
    if c == 0:
        return None
    while c > 0:
        c -= 1
        if lines[r][c] != '.':
            return (r, c)
    return None

def right(lines, r, c):
    if c == num_cols-1:
        return None
    while c < num_cols-1:
        c += 1
        if lines[r][c] != '.':
            return (r, c)
    return None

def top_left(lines, r, c):
    if r == 0 or c == 0:
        return None
    while r > 0 and c > 0:
        r -= 1
        c -= 1
        if lines[r][c] != '.':
            return (r, c)
    return None

def top_right(lines, r, c):
    if r == 0 or c == num_cols-1:
        return None
    while r > 0 and c < num_cols-1:
        r -= 1
        c += 1
        if lines[r][c] != '.':
            return (r, c)
    return None

def bottom_left(lines, r, c):
    if r == num_rows-1 or c == 0:
        return None
    while r < num_rows-1 and c > 0:
        r += 1
        c -= 1
        if lines[r][c] != '.':
            return (r, c)
    return None

def bottom_right(lines, r, c):
    if r == num_rows-1 or c == num_cols-1:
        return None
    while r < num_rows-1 and c < num_cols-1:
        r += 1
        c += 1
        if lines[r][c] != '.':
            return (r, c)
    return None

def rule1(lines, r, c) -> bool:
    if lines[r][c] != 'L':
        return False

    upt = up(lines, r, c)
    if upt and lines[upt[0]][upt[1]] == '#':
        return False

    downt = down(lines,r,c)
    if downt and lines[downt[0]][downt[1]] == '#':
        return False

    leftt = left(lines,r,c)
    if leftt and lines[leftt[0]][leftt[1]] == '#':
        return False

    rightt = right(lines, r, c)
    if rightt and lines[rightt[0]][rightt[1]] == '#':
        return False

    # top left
    tlt = top_left(lines, r, c)
    if tlt and lines[tlt[0]][tlt[1]] == '#':
        return False

    # top right
    trt = top_right(lines, r, c)
    if trt and lines[trt[0]][trt[1]] == '#':
        return False

    # bottom left
    blt = bottom_left(lines, r, c)
    if blt and lines[blt[0]][blt[1]] == '#':
        return False

    # bottom right
    brt = bottom_right(lines, r, c)
    if brt and lines[brt[0]][brt[1]] == '#':
        return False
    return True


def rule2(lines, r, c) -> bool:
    if lines[r][c] != '#':
        return False

    num_occ = 0
    upt = up(lines, r, c)
    if upt and lines[upt[0]][upt[1]] == '#':
        num_occ += 1

    downt = down(lines, r, c)
    if downt and lines[downt[0]][downt[1]] == '#':
        num_occ += 1

    leftt = left(lines, r, c)
    if leftt and lines[leftt[0]][leftt[1]] == '#':
        num_occ += 1

    rightt = right(lines, r, c)
    if rightt and lines[rightt[0]][rightt[1]] == '#':
        num_occ += 1

    # top left
    tlt = top_left(lines, r, c)
    if tlt and lines[tlt[0]][tlt[1]] == '#':
        num_occ += 1

    # top right
    trt = top_right(lines, r, c)
    if trt and lines[trt[0]][trt[1]] == '#':
        num_occ += 1

    # bottom left
    blt = bottom_left(lines, r, c)
    if blt and lines[blt[0]][blt[1]] == '#':
        num_occ += 1

    # bottom right
    brt = bottom_right(lines, r, c)
    if brt and lines[brt[0]][brt[1]] == '#':
        num_occ += 1
    if num_occ >= 5:
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
print(occ) # part 2