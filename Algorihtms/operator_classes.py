from operator import *

class MyObj:
    """Пример перегрузки операторов"""
    def __init__(self, val):
        super(MyObj, self).__init__()
        self.val = val

    def __str__(self):
        return 'MyObj({})'.format(self.val)

    def __lt__(self, other):
        """Сравнение меньше чем"""
        print('Testing {} < {}'.format(self, other))
        return self.val < other.val

    def __add__(self, other):
        """Суммирование значений"""
        print('Adding {} + {}'.format(self, other))
        return MyObj(self.val + other.val)

a = MyObj(1)
b = MyObj(2)

print('Comparison:')
print(lt(a, b))
print('\nArithmetic:')
print(add(a, b))

