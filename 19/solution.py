from typing import List
import functools

with open('input3') as f:
    lines = [x.strip() for x in f]

# for line in lines:
#     print(line)

sep = lines.index('')
rules = lines[:sep]
messages = lines[sep+1:]

print('-'*44)
for r in rules:
    print(r)

rules = [r.replace('"', '') for r in rules]
rules = [r.split(':') for r in rules]
rules = {int(r[0]):r[1].split('|') for r in rules}

def inty(s):
    try: return int(s)
    except: return s

def format(li):
    for i in range(len(li)):
        li[i] = list(map(inty, li[i].strip().split(' ')))

[format(v) for _,v in rules.items()]

for r in rules.items():
    print(r)


# fix rule 8
# ftall = []
# ft = []
# for i in range(4):
#     ft.append(42)
#     ftall.append(ft.copy())
# #print(ftall)
# rules[8] = ftall
# print('rule8', rules[8])

# fix rule 11
# ftall = []
# ft = []
# for i in range(1,3):
#     ft = [42] * i + [31] * i
#     ftall.append(ft.copy())
# #print(ftall)
# rules[11] = ftall
# print('rule11', rules[11])


print('\n\n-----')

def get_all_combinations(li) -> List[str]: # fix this this is wrong
    # for i in range(len(li)):
    #     li[i] = set(li[i])
    print(li)
    if len(li) == 1:
        return li[0]
    first = li[0]
    combs = get_all_combinations(li[1:])
    out = set()
    for f in first:
        for c in combs:
            new_str = f+c
            if len(new_str) < 100:
                out.add(f + c)
    return out


# generate all valid strings
@functools.lru_cache()
def solve_rules(rule: int) -> List[str]:
    rule_val = rules[rule]
    if rule_val[0] == ['a'] or rule_val[0] == ['b']:
        return {rule_val[0][0]}
    if len(rule_val) == 1:
        nums = rule_val[0]
        res = [solve_rules(n) for n in nums]
        return get_all_combinations(res)
    else: #if len(rule_val) == 2:
        res_list = []
        for num in rule_val:
            res_list.append([solve_rules(n) for n in num])
        all_combs = [get_all_combinations(r) for r in res_list]
        return set.union(*all_combs)

## 99, 86
all_allowed = solve_rules(0)
print('len all allowed: ', len(all_allowed))
print()

cnt = 0
for m in messages:
    if m in all_allowed:
        cnt += 1
print(cnt)


print(solve_rules(42))

# # dfs
# def solve_message(s:str, rule: int) -> bool:
#     rule_val = rules[rule]
#     assert len(rule_val) in {1, 2}
#     if len(rule_val) == 1:
#         first_num = rule_val[0][0]
#         allow_set = solve_rules(first_num)
#         for allowed in allow_set:
#             if s.startswith(allowed):
#                 pass
#
#     elif len(rule_val) == 2:
#         nums1 = rule_val[0]
#         nums2 = rule_val[1]
#         res1 = [solve_rules(n) for n in nums1]
#         res2 = [solve_rules(n) for n in nums2]
#        # print(res1, get_all_combinations(res1), res2, '-----')
#         return get_all_combinations(res1) + get_all_combinations(res2)
#
#

 #   if not s.startswith(prxxxe):
 #       return False



# ans = solve_message('ababbb', 0)
# print(ans)
#





