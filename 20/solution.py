import math
import copy
import itertools
import re

with open('input') as f:
    lines = [x.strip() for x in f]

tiles = []
tile = []
for line in lines:
    if line == '':
        tiles.append(tile)
        tile = []
    else:
        tile.append(line)
tiles = {int(t[0].split()[1][:-1]): t[1:] for t in tiles}

class Tile:
    def __init__(self, id:int, li: list):
        self.id = id
        self.tile = li
        self.state = 0
        self.all_states = self.get_all_states()

    def __repr__(self):
        out = str(self.id) + '\n'
        for row in self.tile:
            out += row + '\n'
        return out

    def set_state(self, i: int):
        self.tile = self.all_states[i]
        self.state = i

    @staticmethod
    def rotate_right(li: list):
        num_rows, num_cols = len(li), len(li[0])
        out = []
        for col in range(num_cols):
            new_row = ''
            for row in range(num_rows-1, -1, -1):
                new_row += li[row][col]
            out.append(new_row)
        return out

    @staticmethod
    def fliplr(li: list):
        return [row[::-1] for row in li]

    def get_all_states(self):
        out = [self.tile]
        for _ in range(3):
            out.append(self.rotate_right(out[-1]))
        out.append(self.fliplr(out[-1]))
        for _ in range(3):
            out.append(self.rotate_right(out[-1]))
        return out

    def get_top(self):
        return self.tile[0]

    def get_bottom(self):
        return self.tile[-1]

    def get_right(self):
        out = []
        [out.append(t[-1]) for t in self.tile]
        return ''.join(out)

    def get_left(self):
        out = []
        [out.append(t[0]) for t in self.tile]
        return ''.join(out)

    def right_match(self, t: 'Tile') -> bool:
        if self.get_right() == t.get_left():
            return True
        return False

    def bottom_match(self, t: 'Tile') -> bool:
        if self.get_bottom() == t.get_top():
            return True
        return False


# create tile objects
tilesobj = {}
for k,v in tiles.items():
    tilesobj[k] = Tile(k, v)

SIDE_LENGTH = round(math.sqrt(len(tiles)))

# check tile in its current state can go there
def fit_piece(current_image: dict, rc: tuple, tile: Tile):
    row, col = rc
    if col > 0: # check left
        left = (row, col-1)
        if left in current_image and not current_image[left].right_match(tile):
            return False

    if col < SIDE_LENGTH-1: # check right
        right = (row, col+1)
        if right in current_image and not tile.right_match(current_image[right]):
            return False

    if row > 0: # check top
        top = (row-1, col)
        if top in current_image and not current_image[top].bottom_match(tile):
            return False

    if row < SIDE_LENGTH-1: # check bottom
        bottom = (row+1, col)
        if bottom in current_image and not tile.bottom_match(current_image[bottom]):
            return False

    return True

def solve_image(current_image, possibilities, rd):
    if len(current_image) == len(tilesobj):
        return current_image
    for row in range(SIDE_LENGTH):
        for col in range(SIDE_LENGTH):
            if (row, col) not in current_image: # found empty spot
                # select a tile to place
                for ID in possibilities:
                    tile = tilesobj[ID]
                    for state in range(8):
                        tile.set_state(state)
                        if fit_piece(current_image, (row, col), tile):
                            new_current_image = copy.deepcopy(current_image)
                            new_current_image[(row, col)] = tile
                            new_possibilities = possibilities.copy()
                            new_possibilities.remove(ID)
                            out = solve_image(new_current_image, new_possibilities, rd+1)
                            if out is not False:
                                return out
                return False

current_image = {}  # (row, col) -> tile, if present
possibilities = set(tilesobj.keys())
image = solve_image(current_image, possibilities, 0)
corners = list(itertools.product((0, SIDE_LENGTH-1), repeat=2))
prod = math.prod([image[c].id for c in corners])
print('part1:', prod)

############# part 2
# remove borders
for k,v in image.items():
    v.tile = [x[1:-1] for x in v.tile[1:-1]]

# glue together
def add_tiles_horizontal(li1: list, li2: list):
    out = []
    for i in range(len(li1)):
        out.append(li1[i] + li2[i])
    return out

col_sum_all = []
for row in range(SIDE_LENGTH):
    col_sum = image[(row, 0)].tile
    for col in range(1, SIDE_LENGTH):
        col_sum = add_tiles_horizontal(col_sum, image[(row, col)].tile)
    col_sum_all.append(col_sum)

clean_image = sum(col_sum_all, []) # list of str

m1 = '                  # '
m2 = '#    ##    ##    ###'
m3 = ' #  #  #  #  #  #   '
m1_idx = [m.start() for m in re.finditer('#', m1)]
m2_idx = [m.start() for m in re.finditer('#', m2)]
m3_idx = [m.start() for m in re.finditer('#', m3)]

def match_monster(r1, r2, r3):
    for idx in m1_idx:
        if r1[idx] != '#': return False
    for idx in m2_idx:
        if r2[idx] != '#': return False
    for idx in m3_idx:
        if r3[idx] != '#': return False
    return True

def get_num(clean_image):
    is_monster = set()
    for row in range(len(clean_image) - 3 + 1):
        for col in range(len(clean_image[0]) - len(m1)+1):
            r1 = clean_image[row][col: col + len(m1)]
            r2 = clean_image[row+1][col: col + len(m1)]
            r3 = clean_image[row + 2][col: col + len(m1)]
            if match_monster(r1, r2, r3):
                for idx in m1_idx:
                    is_monster.add((row, col+idx))
                for idx in m2_idx:
                    is_monster.add((row+1, col+idx))
                for idx in m3_idx:
                    is_monster.add((row+2, col+idx))

    size_monsters = len(is_monster)
    ct_hash = 0
    for st in clean_image:
        for c in st:
            if c == '#':
                ct_hash += 1
    return ct_hash - size_monsters

def get_all_states(clean_image):
    out = [clean_image]
    for _ in range(3):
        out.append(Tile.rotate_right(out[-1]))
    out.append(Tile.fliplr(out[-1]))
    for _ in range(3):
        out.append(Tile.rotate_right(out[-1]))
    return out

ans_li = [get_num(x) for x in get_all_states(clean_image)]
print('part2:', min(ans_li))
