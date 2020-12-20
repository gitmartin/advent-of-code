with open('input') as f:
    lines = [x.strip().replace(' ','') for x in f]

def reduce_plus(st):
    if len(st) >= 3 and st[-1].isdigit() and st[-2] in {'+'} and st[-3].isdigit():
        res = eval(st[-3] + st[-2] + st[-1])
        del st[-3:]
        st.append(str(res))

def get_ans(line):
    st = [] # stack
    for c in line:
        reduce_plus(st)
        if c == ')':
            ind = len(st) - 1
            while st[ind] != '(': # find '('
                ind -= 1
            eval_str = ''.join(st[ind+1:])
            st = st[:ind+1]
            st[ind] = str(eval(eval_str))
        elif c.isdigit() or c in {'+', '*', '('}:
            st.append(c)
    reduce_plus(st)
    return eval(''.join(st))

print(sum([get_ans(m) for m in lines]))
