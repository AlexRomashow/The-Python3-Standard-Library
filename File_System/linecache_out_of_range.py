import linecache
from linecache_data import *

filename = make_tempfile()
# Кеш всегда возвращает строку, используя пустую строку для
# указания того, что запрошенная строка не существует
not_there = linecache.getline(filename, 500)
print('NOT THERE: {!r} includes {} characters'.format(
    not_there, len(not_there)))

cleanup(filename)
