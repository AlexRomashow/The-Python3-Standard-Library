import bz2
import os

data = 'Character with an ąccent.'

with bz2.open('example.bz2', 'wt', encoding='utf-8') as output:
    output.write(data)

with bz2.open('example.bz2', 'rt', encoding='utf-8') as input:
    print('Full file: {}'.format(input.read()))

# Переместиться в начало символа c акцентом
with bz2.open('example.bz2') as input:
    input.seek(18)
    print('One character: {}'.format(input.read(1)))

# Переместиться в середину символа c акцентом
with bz2.open('example.bz2', 'rt', encoding='utf-8') as input:
    input.seek(19)
    try:
        print(input.read(1))
    except UnicodeDecodeError:
        print('ERROR: failed to decode')











