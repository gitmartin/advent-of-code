f = open('input')
lines = f.readlines()
numbers = [int(x.strip()) for x in lines]
print(len(numbers))
for n in numbers:
    if 2020 - n in numbers:
        print('solution', n*(2020-n))
print(numbers)


for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j+1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                print('solution2', numbers[i] * numbers[j] * numbers[k])