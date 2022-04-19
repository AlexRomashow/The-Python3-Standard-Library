from operator import *

class MyObj:
    """Образец класса для attrgetter"""
    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return 'MyObj({})'.format(self.arg)

l = [MyObj(i) for i in range(5)]
print('objects:', l)

# Извлечение значения 'arg' из каждого объекта
g = attrgetter('arg')
vals = [g(i) for i in l]
print('arg values:', vals)

# Сортировка c использованием arg
l.reverse()
print('reversed ;', l)
print('sorted:', sorted(l, key=g))
