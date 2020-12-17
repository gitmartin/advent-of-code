import copy
import math

with open('input') as f:
    lines = [x.strip() for x in f]

def inty(li):
    return [int(x) for x in li]

fields = lines[:20]
ticket = lines[22]
nb_tickets = lines[25:]
ticket = inty(ticket.split(','))
nb_tickets = [inty(t.split(',')) for t in nb_tickets]

all_ranges = []
for f in fields:
    ranges = f.split(': ')[1].split(' or ')
    ranges = [r.split('-') for r in ranges]
    ranges = [inty(x) for x in ranges]
    all_ranges.append(ranges)

def is_valid(num):
    for r1, r2 in all_ranges:
        if r1[0] <= num <= r1[1] or r2[0] <= num <= r2[1]:
            return True
    return False

def ticket_is_valid(li):
    cnt = 0
    for num in li:
        if not is_valid(num):
            cnt += num
    return cnt

out = 0
for t in nb_tickets:
    out += ticket_is_valid(t)
print('part 1:', out)

def check_candidate(col, r):
    r1, r2 = r
    for num in col:
        if not (r1[0] <= num <= r1[1] or r2[0] <= num <= r2[1]):
            return False
    return True

valid_nb_tickets = [t for t in nb_tickets if ticket_is_valid(t) == 0]

candidates = {} # pos -> allowed ranges

for pos in range(len(valid_nb_tickets[0])): # for each pos
    col = [t[pos] for t in valid_nb_tickets] # all the i'th numbers in the tickets
    cand = set()
    for r_pos in range(len(all_ranges)):
        r = all_ranges[r_pos]
        if check_candidate(col, r):
            cand.add(r_pos)
    candidates[pos] = cand

t = [(k,v,len(v)) for k,v in candidates.items()]
t = sorted(t, key=lambda x:x[2])
candidates = {x[0]:x[1] for x in t}

def solved(candidates):
    for k, v in candidates.items():
        if len(v) != 1:
            return False
    return True

def check_broken(candidates):
    for k, v in candidates.items():
        if len(v) == 0:
            return True
    return False

def solve(candidates):
    if solved(candidates):
        return True, candidates
    if check_broken(candidates):
        return False, None
    for k, v in candidates.items():
        if len(v) > 1:
            for choice in v:
                new_candidates = copy.deepcopy(candidates)
                for nk, nv in new_candidates.items():
                    nv.discard(choice)
                new_candidates[k] = {choice}
                sol, cands = solve(new_candidates)
                if sol:
                    return sol, cands

sol, cands = solve(candidates)
sol_positions = [k for k, v in cands.items() if v.pop() in range(6)]
sol = [ticket[x] for x in sol_positions]
print('part 2:', math.prod(sol))
