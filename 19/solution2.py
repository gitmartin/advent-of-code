from typing import List
import functools

# parse input
with open('input') as f:
    lines = [x.strip() for x in f]
sep = lines.index('')
rules = lines[:sep]
messages = lines[sep+1:]
rules = [r.replace('"', '') for r in rules]
rules = [r.split(':') for r in rules]
rules = {int(r[0]): r[1].split('|') for r in rules}

def inty(s):
    try: return int(s)
    except: return s

def format(li):
    for i in range(len(li)):
        li[i] = list(map(inty, li[i].strip().split(' ')))

[format(v) for _, v in rules.items()]

#fix rule 8 with a hack
ftall = []
ft = []
for i in range(6):
    ft.append(42)
    ftall.append(ft.copy())
rules[8] = ftall
#print('rule8', rules[8])

# fix rule 11 with a hack
ftall = []
ft = []
for i in range(1,6):
    ft = [42] * i + [31] * i
    ftall.append(ft.copy())
rules[11] = ftall
#print('rule11', rules[11])

def get_all_combinations(li, rule, s: str) -> set:
    if len(li) == 1:
        return li[0]
    first = li[0]
    combs = get_all_combinations(li[1:], rule, s)
    out = set()
    for f in first:
        for c in combs:
            new_str = f+c
            if new_str in s:  # this is a total hack... speeds things up.
                out.add(new_str)
    return out

@functools.lru_cache()
def solve_rules(rule: int, s: str) -> List[str]:
    rule_val = rules[rule]
    if rule_val[0] == ['a'] or rule_val[0] == ['b']:
        return {rule_val[0][0]}
    res_list = []
    for num in rule_val:
        res_list.append([solve_rules(n, s) for n in num])
    all_combs = [get_all_combinations(r, rule, s) for r in res_list]
    return set.union(*all_combs)

cnt = 0
for m in messages:
    possibilities = solve_rules(0, m)
    if m in possibilities:
        cnt += 1
print(cnt)
