import codecs
import sys

from codecs_to_hex import to_hex

error_handling = sys.argv[1]

text = 'français'
print('Original:', repr(text))

# Сохранить данные c использованием некоторой кодировки
with codecs.open('decode_error.txt', 'w',
                    encoding='utf-16') as f:
    f.write(text)

# Вывести байтовое содержимое файла
with open('decode_error.txt', 'rb') as f:
    print('File contents:', to_hex(f.read(), 1))

# Попытаться прочитать данные c использованием неверной кодировки
with codecs.open('decode_error.txt', 'r',
            encoding='utf-8',
            errors=error_handling) as f:
    try:
        data = f.read()
    except UnicodeDecodeError as err:
        print('ERROR:', err)
    else:
        print('Read:', repr(data))
