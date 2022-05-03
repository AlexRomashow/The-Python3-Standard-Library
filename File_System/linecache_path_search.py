import linecache
import os

# Поиск модуля linecache c использованием пути,
# указанного в sys.path
module_line = linecache.getline('linecache.py', 3)
print('MODULE:')
print(repr(module_line))

# Непосредственный поиск модуля linecache
file_src = linecache.__file__
if file_src.endswith('.pyc'):
    file_src = file_src[:-1]
print('\nFILE:')
with open(file_src, 'r') as f:
    file_line = f.readlines()[2]
print(repr(file_line))
