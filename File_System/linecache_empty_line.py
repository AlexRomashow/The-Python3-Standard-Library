import linecache
from linecache_data import *

filename = make_tempfile()

# Пустые строки включают символ перевода строки
print('BLANK : {!r}'.format(linecache.getline(filename, 8)))
cleanup(filename)
