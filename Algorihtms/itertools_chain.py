from itertools import chain

for i in chain([1, 2, 4], ['a', 'b', 'c']):
    print(i, end=' ')
print()
