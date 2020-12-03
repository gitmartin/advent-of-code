import math

with open('input') as f:
    hill = [line.strip() for line in f]
width = len(hill[0])


def get_num_trees(direction):
    right, down = direction[0], direction[1]
    trees = 0
    col = 0
    for row in range(0, len(hill), down):
        print(hill[row])
        if hill[row][col % width] == '#':
            trees += 1
        col += right
    return trees


out = get_num_trees((3, 1))
paths = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
out = math.prod(map(get_num_trees, paths))
print(out)

