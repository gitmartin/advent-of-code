import numpy as np

with open('input') as f:
    lines = [(x.strip()) for x in f]

pos = np.array([0, 0])
way_pos = np.array([10, 1])
rotation_matrix = np.array([[0, -1],[1, 0]]) # 90 left

def move_way(pos: list, dir: str, mag: int):
    if dir == 'N':
        pos[1] += mag
    elif dir == 'S':
        pos[1] -= mag
    elif dir == 'E':
        pos[0] += mag
    elif dir == 'W':
        pos[0] -= mag

for inst in lines:
    dir = inst[0]
    mag = int(inst[1:])
    if dir in {'N', 'S', 'E', 'W'}:
        move_way(way_pos, dir, mag)
    elif dir == 'F':
        pos += way_pos * mag
    else:
        factor = 1 if dir == 'L' else -1
        times = round(mag / 90)
        way_pos = np.linalg.matrix_power(factor*rotation_matrix, times) @ way_pos

print(np.linalg.norm(pos, 1)) # part 2
