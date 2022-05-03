import linecache

# Если модулю linecache не удается найти файл, то ошибка скрывается
no_such_file = linecache.getline(
    'this_file_does_not_exist.txt', 1,)

print('NO FILE: {!r}'.format(no_such_file))
