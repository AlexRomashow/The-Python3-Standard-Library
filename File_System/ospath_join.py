import os.path

PATHS = [
    ('one', 'two', 'three'),
    ('/', 'one', 'two', 'threr'),
    ('/one', '/two', '/three'),
]

for parts in PATHS:
    print('{} : {!r}'.format(parts, os.path.join(*parts)))
