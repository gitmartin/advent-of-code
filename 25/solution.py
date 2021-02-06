MOD = 20201227
card_pk = 15113849
door_pk = 4206373

def get_loop_size(pk):
    val = 1
    ls = 1
    while True:
        val *= 7
        val = val % MOD
        if val == pk:
            return ls
        ls += 1

def transform(inp, ls):
    val = 1
    for _ in range(ls):
        val *= inp
        val = val % MOD
    return val

x = get_loop_size(card_pk)
out = transform(door_pk, x)
print(out)
