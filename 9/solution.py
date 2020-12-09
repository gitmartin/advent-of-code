with open('input') as f:
    lines = [int(x.strip()) for x in f]

def is_sum(s: set, num: int):
    for k in s:
        if num - k in s:
            return True
    return False

for pos in range(25, len(lines)):
    if not is_sum(lines[pos-25:pos], lines[pos]):
        print(lines[pos])
        break

target = 731031916
for i in range(len(lines)):
    for j in range(i+2, len(lines)):
        s = sum(lines[i:j])
        if s == target:
            sol = lines[i:j]
            print('found it ')
print(min(sol) + max(sol))
