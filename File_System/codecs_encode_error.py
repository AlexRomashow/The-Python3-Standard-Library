import codecs
import sys

error_handling = sys.argv[1]

text = 'fraтçais'

try:
    # Сохранить данные в кодировке ASCII, используя режим
    # обработки ошибок, указанный в командной строке
    with codecs.open('encode_error.txt', 'w',
            encoding='ascii',
            errors=error_handling) as f:
        f.write(text)
except UnicodeEncodeError as err:
    print('ERROR:', err)
else:
    # В случае отсутствия ошибок при записи в файл отобразить
    # его содержимое
    with open('encode_error.txt', 'rb') as f:
        print('File contents: {!r}'.format(f.read()))
