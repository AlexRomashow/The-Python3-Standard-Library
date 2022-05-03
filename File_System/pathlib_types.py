import itertools
import os
import pathlib

root = pathlib.Path('test_files')

# Удаление объектов, созданных во время предыдущих запусков
if root.exists():
    for f in root.iterdir():
        f.unlink()
else:
    root.mkdir()

# Создание тестовых файлов
(root / 'file').write_text(
    'This is а regular file', encoding='utf-8')
(root / 'symlink').symlink_to('file')
os.mkfifo(str(root / 'fifo'))

# Проверка типов файлов
to_scan = itertools.chain(
    root.iterdir(),
    [pathlib.Path('/dev/diskO'),
    pathlib.Path('/dev/console')],
)
hfmt = '{:18s}' + (' {:>5} ' * 6)
print(hfmt.format('Name', 'File', 'Dir', 'Link', 'FIFO', 'Block', 'Character'))
print()

fmt = '{:20s} ' + (' {!r:>5} ' * 6)
for f in to_scan:
    print(fmt.format(
        str(f),
        f.is_file(),
        f.is_dir(),
        f.is_symlink(),
        f.is_fifo(),
        f.is_block_device(),
        f.is_char_device(),
))

