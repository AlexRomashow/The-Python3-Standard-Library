import filecmp
import os

# Определение элементов, существующих в обоих каталогах
d1_contents = set(os.listdir('example/dir1'))
d2_contents = set(os.listdir('example/dir2'))
common = list(d1_contents & d2_contents)
common_files = [
    f
    for f in common
    if os.path.isfile(os.path.join('example/dirl', f))
]
print('Common files:', common_files)

# Сравнение каталогов
match, mismatch, errors = filecmp.cmpfiles(
    'example/dir1',
    'example/dir2',
    common_files,
)
print('Match:', match)
print('Mismatch:', mismatch)
print('Errors:', errors)
