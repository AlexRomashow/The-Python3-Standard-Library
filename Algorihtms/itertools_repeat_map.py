from itertools import *

for i in map(lambda x, y: (x, y, x * y), repeat(2), range(50)):
    print('{:d} * {:d} = {:d}'.format(*i))
