import numpy as np

with open('input') as f:
    lines = [int(x.strip()) for x in f]
lines.sort()
lines_set = set(lines)

ar = np.array(lines)
d = np.diff(ar)
part1 = (sum(d == 1) + 1) * (sum(d == 3) + 1)
#print(part1)

maxi = lines[-1] # have to end up with this
memo = {} # jolt: # ways to get to 0

def num_ways(n, memo):
    if n not in lines_set:
        return 0
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n == 2:
        return 1 + num_ways(1, memo)
    if n == 3:
        return 1 + num_ways(1, memo) + num_ways(2, memo)
    num_n = num_ways(n-1, memo) + num_ways(n-2, memo) + num_ways(n-3, memo)
    memo[n] = num_n
    return num_n

print(num_ways(maxi, memo)) # part 2
