import numpy as np

def get_cards():
    with open('input') as f:
        lines = [x.strip() for x in f]
    lines.append('')
    cards = []
    player = []
    for line in lines:
        if line == '':
            cards.append(player)
            player = []
        else:
            player.append(line)
    return [list(map(int, c[1:])) for c in cards]

cards = get_cards()
while cards[0] and cards[1]:
    p1 = cards[0].pop(0)
    p2 = cards[1].pop(0)
    if p1 > p2:
        cards[0].append(p1)
        cards[0].append(p2)
    elif p2 > p1:
        cards[1].append(p2)
        cards[1].append(p1)

win = cards[0] if cards[0] else cards[1]
vec = np.arange(len(win)-1, -1, -1) + 1
print('part1:', vec @ win)

def to_tup(li):
    return (tuple(li[0]), tuple(li[1]))

def game(cards):
    seen = set()
    while cards[0] and cards[1]:
        tup = to_tup(cards)
        if tup in seen:
            return 0, cards[0]
        seen.add(tup)
        p0 = cards[0].pop(0)
        l0 = len(cards[0])
        p1 = cards[1].pop(0)
        l1 = len(cards[1])
        if l0 >= p0 and l1 >= p1:
            new_car0 = cards[0][:p0]
            new_car1 = cards[1][:p1]
            new_cards = [new_car0, new_car1]
            winner, _ = game(new_cards)
            if winner == 0:
                cards[0].append(p0)
                cards[0].append(p1)
            else:
                cards[1].append(p1)
                cards[1].append(p0)
            continue
        if p0 > p1:
            cards[0].append(p0)
            cards[0].append(p1)
        elif p1 > p0:
            cards[1].append(p1)
            cards[1].append(p0)
    if cards[0]:
        return 0, cards[0]
    return 1, cards[1]

cards = get_cards()
_, win = game(cards)
vec = np.arange(len(win)-1, -1, -1) + 1
print('part2:', win @ vec)
