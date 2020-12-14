# https://en.wikipedia.org/wiki/Chinese_remainder_theorem
with open('input') as f:
    lines = [(x.strip()) for x in f]

buses = enumerate(lines[1].split(','))
buses = [(b[0], int(b[1])) for b in buses if b[1] != 'x']
eqns = [((b[1] - b[0])%b[1], b[1]) for b in buses] # put in equation form, i.e. x = a_1 (mod n_1). tuples are (a_1, n_1)

# extended Euclidean algorithm
def bezout(a, b):
    prev = [a, 1, 0]
    now = [b, 0, 1]
    while True:
        q, _ = divmod(prev[0], now[0])
        z = zip(prev, now)
        next = [x[0] - q * x[1] for x in z]
        if next[0] == 0:
            break
        prev = now
        now = next
    return now[1:]

def reduce(e1, e2):
    m1, m2 = bezout(e1[1], e2[1])
    x = m1*e1[1]*e2[0] + m2*e2[1]*e1[0]
    mod_prod = e1[1] * e2[1]
    return x % mod_prod, mod_prod

result = eqns[0]
for eq in eqns[1:]:
    result = reduce(result, eq)

print(result[0])
