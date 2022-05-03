import linecache
from linecache_data import *

filename = make_tempfile()

# Выбор одной и той же строки из исходного файла и кеша
# (имейте в виду, что linecache нумерует строки, начиная c 1)

print('SOURCE:')
print('{!r}'.format(lorem.split('\n')[4]))
print()
print('CACHE:')
print('{!r}'.format(linecache.getline(filename, 5)))
cleanup(filename)
