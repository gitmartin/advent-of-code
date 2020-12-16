li = [1, 20, 11, 6, 12, 0]

indeces = {}  # values -> indeces
for i in range(len(li)):
    val = li[i]
    if val in indeces:
        indeces[val].append(i)
    else:
        indeces[val] = [i]

pos = len(li)
val = li[-1]
while pos < 30_000_000:
    if pos % 1_000_000 == 0:
        print(pos)
    if val in indeces and len(indeces[val]) > 1:
        new_val = indeces[val][-1] - indeces[val][-2]
        if new_val in indeces:
            indeces[new_val].append(pos)
        else:
            indeces[new_val] = [pos]
        val = new_val
    else:
        indeces[0].append(pos)
        val = 0
    pos += 1

print(val)
