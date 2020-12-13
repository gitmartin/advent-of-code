import numpy as np

with open('input') as f:
    lines = [(x.strip()) for x in f]

#     [x, y]
pos = [0, 0]
directions = ['N', 'E', 'S', 'W']

def move(pos: list, dir: str, mag: int):
    if dir == 'N':
        pos[1] += mag
    elif dir == 'S':
        pos[1] -= mag
    elif dir == 'E':
        pos[0] += mag
    elif dir == 'W':
        pos[0] -= mag

facing = 1 # 'E'
for inst in lines:
    dir = inst[0]
    mag = int(inst[1:])
    if dir in {'N', 'S', 'E', 'W'}:
        move(pos, dir, mag)
    elif dir == 'F':
        move(pos, directions[facing], mag)
    elif dir == 'L':
        times = round(mag/90)
        facing = (facing - times) % 4
    elif dir == 'R':
        times = round(mag/90)
        facing = (facing + times) % 4

print(np.linalg.norm(pos, 1)) # part 1
