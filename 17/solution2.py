import numpy as np

with open('input') as f:
    lines = [list(map(lambda x: 1 if x == '#' else 0, list(x.strip()))) for x in f]

def rule1(ra, x,y,z, t):
    if ra[x,y,z,t ] == 1:
        s = 0
        for i in range(-1,2):
            for j in range(-1,2):
                for k in range(-1,2):
                    for l in range(-1,2):
                        s += ra[x+i,y+j,z+k,t+l]
        s -= 1
        if s == 2 or s == 3:
            return False
        return True
    return False

def rule2(ra, x,y ,z,t ):
    if ra[x,y,z,t] == 0:
        s = 0
        for i in range(-1,2):
            for j in range(-1,2):
                for k in range(-1,2):
                    for l in range(-1,2):
                       s += ra[x+i,y+j,z+k, t+l]
        if s == 3:
            return True
    return False

inp = np.array(lines)
rows = inp.shape[0]
s = 30
ra = np.zeros((s, s, s, s), dtype=int)
pos = s//2
ra[pos,pos, pos:pos+rows,pos:pos+rows] = inp

for prog in range(6):
    print(prog)
    to_flip = []
    sh = ra.shape
    for i in range(1,sh[0]-1):
        for j in range(1,sh[1]-1):
            for k in range(1,sh[2]-1):
                for l in range(1, sh[3]-1):
                    if rule1(ra,i,j,k,l) or rule2(ra,i,j,k,l):
                        to_flip.append((i,j,k,l))
    for tf in to_flip:
        ra[tf[0],tf[1],tf[2],tf[3]] = 1 - ra[tf[0],tf[1],tf[2],tf[3]]

print(ra.sum())
