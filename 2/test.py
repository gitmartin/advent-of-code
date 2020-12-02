import re

f = open('input')
lines = f.readlines()
lines = [(x.strip()) for x in lines]
lines = [re.split('-| |: ', x) for x in lines]


def count(s: str, c):
    counti = 0
    for char in s:
        if char == c:
            counti += 1
    return counti


print(lines)
good = 0
for passw in lines:
    lo = int(passw[0])
    hi = int(passw[1])
    let = passw[2]
    pa = passw[3]
    actual = count(pa, let)
    if lo <= actual <= hi:
        good += 1


print(good)


good = 0
for passw in lines:
    lo = int(passw[0])
    hi = int(passw[1])
    let = passw[2]
    pa = passw[3]

    cond1 = pa[lo-1] == let or pa[hi-1] == let
    cond2 = pa[lo-1] == let and pa[hi-1] == let

    if cond1 and not cond2:
        good += 1

print(good)