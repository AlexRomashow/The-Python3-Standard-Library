import collections

# Добавление справа
d1 = collections.deque()
d1.extend('abcdefg')
print('extend:', d1)
d1.append('h')
print('apend:', d1)

# Добавление слева
d2 = collections.deque()
d2.extendleft(range(6))
print('extendleft:', d2)
d2.appendleft(6)
print('appendleft:', d2)
