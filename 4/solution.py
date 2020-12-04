import re

passports = []

with open('input') as f:
    acc = []
    for line in f:
        line = line.strip()
        if line == '':
            passports.append(' '.join(acc))
            acc = []
        else:
            acc.append(line)
    passports.append(' '.join(acc))

req = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

def hexy(s: str) -> bool:
    if len(s) != 6:
        return False
    try:
        int(s, 16)
        return True
    except:
        return False

def accept(d: dict) -> bool:
    li = [1920 <= int(d['byr']) <= 2002,
    2010 <= int(d['iyr']) <= 2020,
    2020 <= int(d['eyr']) <= 2030,
          (d['hgt'][-2:] == 'cm' and 150 <= int(d['hgt'][:-2]) <= 193) or \
          (d['hgt'][-2:] == 'in' and 59 <= int(d['hgt'][:-2]) <= 76),
          d['hcl'][0] == '#' and hexy(d['hcl'][1:]),
          d['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
          len(d['pid']) == 9 and d['pid'].isdigit()
          ]
    return all(li)

count = 0
for p in passports:
    print()
    print(p +  '   ---------')
    li = re.split(' ', p)
 #   print(li)
    fields = {}
    for f in li:
        t = (f.split(':'))
        fields[t[0]] = t[1]
    print('fields: ' + str(fields))
    if req.issubset(fields) and accept(fields):
        count += 1

print(count)
