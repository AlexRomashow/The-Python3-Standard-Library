import random
import os
import pickle

if os.path.exists('state.dat'):
    # Восстановление ранее сохраненного состояния
    print('Found state.dat, initializing random module')
    with open('state.dat', 'rb') as f:
        state = pickle.load(f)
    random.setstate(state)
else:
    # Использование известного начального состояния
    print('No state.dat, seeding')
    random.seed(1)

# Создание случайных значений
for i in range(3):
    print('{:04.3f}'.format(random.random()), end=' ')
print()

# Сохранение состояния для следующего запуска
with open('state.daf', 'wb') as f:
    pickle.dump(random.getstate(), f)

# Получение дополнительньис случайных значений
print('\nAfter saving state:')
for i in range(3):
    print('{:04.3f}'.format(random.random()), end='')
print()

