with open('input') as f:
    lines = [x.strip().replace(' ','') for x in f]

def reduce(st):
    if len(st) >= 3 and st[-1].isdigit() and st[-2] in {'+', '*'} and st[-3].isdigit():
        res = eval(st[-3] + st[-2] + st[-1])
        del st[-3:]
        st.append(str(res))

def get_ans(line):
    st = []
    for c in line:
        reduce(st)
        if c== ')':
            temp = st[-1]
            st = st[:-1]
            st[-1] = temp
        elif c in {'+', '*', '('} or c.isdigit():
            st.append(c)
    reduce(st)
    return int(st[0])

print(sum([get_ans(m) for m in lines]))
