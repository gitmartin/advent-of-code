import numpy as np

with open('input') as f:
    lines = [list(map(lambda x: 1 if x == '#' else 0, list(x.strip()))) for x in f]

def rule1(ra, x,y,z):
    if ra[x,y,z] == 1:
        s = 0
        pp = 0
        for i in range(-1,2):
            for j in range(-1,2):
                for k in range(-1,2):
                    pp += 1
                    s += ra[x+i,y+j,z+k]
        s -= 1
        if s == 2 or s == 3:
            return False
        return True
    return False

def rule2(ra, x,y ,z):
    if ra[x,y,z] == 0:
        s = 0
        for i in range(-1,2):
            for j in range(-1,2):
                for k in range(-1,2):
                    s += ra[x+i,y+j,z+k]
        if s == 3:
            return True
    return False

inp = np.array(lines)
rows = inp.shape[0]
s = 30
ra = np.zeros((s, s, s), dtype=int)
pos = s//2
ra[pos,pos:pos+rows,pos:pos+rows] = inp

for _ in range(6):
    to_flip = []
    sh = ra.shape
    for i in range(1,sh[0]-1):
        for j in range(1,sh[1]-1):
            for k in range(1,sh[2]-1):
                if rule1(ra,i,j,k) or rule2(ra,i,j,k):
                    to_flip.append((i,j,k))
    for tf in to_flip:
        ra[tf[0],tf[1],tf[2]] = 1 - ra[tf[0],tf[1],tf[2]]

print(ra.sum())
