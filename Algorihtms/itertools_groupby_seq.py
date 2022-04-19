import functools
from itertools import *
import operator
import pprint

@functools.total_ordering
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __gt__(self, other):
        return (self.x, self.y) > (other.x, other.y)

# Создание набора данных из экземпляров Point
data = list(map(Point, cycle(islice(count(), 3)), islice(count(), 7)))
print('Data:')
pprint.pprint(data, width=35)
print()

# Попытаться сгруппировать несортированные данные
# на основании значений X
print('Grouped, unsorted:')
for k, g in groupby(data, operator.attrgetter('x')):
    print(k, list(g))
print()

# Сортировка данных
data.sort()
print('Sorted:')
pprint.pprint(data, width=35)
print()

# Группирование сортированных данных на основании значений X
print('Grouped, sorted:')
for k, g in groupby(data, operator.attrgetter('x')):
    print(k, list(g))
print()
