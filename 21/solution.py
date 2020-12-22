from collections import defaultdict, Counter

with open('input') as f:
    lines = [x.strip() for x in f]

foods = {}
for i in range(len(lines)): # line in lines:
    line = lines[i]
    ingr, allerg = line.split(' (contains ')
    ingr = ingr.split()
    allerg = allerg[:-1].split(',')
    allerg = [x.strip() for x in allerg]
    foods[i] = {'ingr': set(ingr), 'allerg': set(allerg)}

allerg = defaultdict(list) # allergen -> foods
for k,v in foods.items():
    for al in v['allerg']:
        allerg[al].append(k)

candidates = {}
for k, v in allerg.items():
    inter = set.intersection(*[foods[num]['ingr'] for num in v])
    candidates[k] = inter

all_ingr = []
for k, v in foods.items():
    all_ingr += list(v['ingr'])

cnt = Counter(all_ingr)
for i in set.union(*candidates.values()):
    del cnt[i]

print('part1:', sum(cnt.values())) # part 1

cands = list(sorted(candidates.items(), key=lambda x: (len(x[1]), x[0])))
for i in range(len(cands)):
    if i > 0:
        to_discard = set.union(*[x[1] for x in cands[:i]])
        for td in to_discard:
            cands[i][1].discard(td)
cands = sorted(cands, key=lambda x: x[0])

ans = [x[1].pop() for x in cands]
print('part2:', ','.join(ans))
