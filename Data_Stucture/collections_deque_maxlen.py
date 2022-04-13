import collections
import random

# Установить для random затравочное значение, чтобы обеспечить
# получение одного и того же вывода при каждом запуске сценария
random.seed(1)

d1 = collections.deque(maxlen=3)
d2 = collections.deque(maxlen=3)

for i in range(5):
    n = random.randint(0, 100)
    print('n =', n)
    d1.append(n)
    d2.appendleft(n)
    print('D1:', d1)
    print('D2:', d2)
