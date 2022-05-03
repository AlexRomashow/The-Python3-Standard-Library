from codecs_to_hex import to_hex

import codecs
import sys

encoding = sys.argv[1]
filename = encoding + '.txt'

print('Write to', filename)
with codecs.open(filename, mode='w', encoding=encoding) as f:
    f.write('français')

# Определение группирования байтов для использования c to_hex()
nbytes = {
    'utf-8': 1,
    'utf-16': 2,
    'utf-32': 4,
}.get(encoding, 1)

# Отображение "сырых" байтов, хранящихся в файле
print('File contents:')
with open(filename, mode='rb') as f:
    print(to_hex(f.read(), nbytes))
