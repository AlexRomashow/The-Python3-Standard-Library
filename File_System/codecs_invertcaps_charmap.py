import codecs
import string

# Отобразить каждый символ на самого себя
decoding_map = codecs.make_identity_dict(range(256))

# Создать список пар порядковых значений для букв
# в верхнем и нижнем регистрах
pairs = list(zip(
    [ord(c) for c in string.ascii_lowercase],
    [ord(c) for c in string.ascii_uppercase],
))

# Изменить отображение для преобразования букв
# верхнего регистра в нижний и наоборот
decoding_map.update({
    upper: lower
    for (lower, upper)
    in pairs
})
decoding_map.update({
    lower: upper
    for (lower, upper)
    in pairs
})

# Создать отдельную кодирующую таблицу
encoding_map = codecs.make_encoding_map(decoding_map)

if __name__ == '__main__':
    print(codecs.charmap_encode('abcDEF', 'strict',
                            encoding_map))
    print(codecs.charmap_decode(b'abcDEF', 'strict',
                            decoding_map))
    print(encoding_map == decoding_map)
