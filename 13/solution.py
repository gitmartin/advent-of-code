import numpy as np
with open('input') as f:
    lines = [(x.strip()) for x in f]
ts = int(lines[0])
buses = lines[1].split(',')
buses = np.array([int(b) for b in buses if b != 'x'])
frac = ts/buses
minutes_to_wait = (1 - frac % 1)*buses
am = np.argmin(minutes_to_wait)
print(minutes_to_wait[am] * buses[am]) # part 1
