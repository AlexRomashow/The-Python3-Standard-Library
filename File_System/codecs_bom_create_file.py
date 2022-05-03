import codecs
from codecs_to_hex import to_hex

# Выбрать несобственную версию кодировки UTF-16
if codecs.BOM_UTF16 == codecs.BOM_UTF16_BE:
    bom = codecs.BOM_UTF16_LE
    encoding = 'utf_16_le'
else:
    bom = codecs.BOM_UTF16_BE
    encoding = 'utf_16_be'

print('Native order:', to_hex(codecs.BOM_UTF16, 2))
print('Selected order:', to_hex(bom, 2))

# Кодирование текста
encoded_text = 'français'.encode(encoding)
print('{:14}: {}'.format(encoding, to_hex(encoded_text, 2)))

with open('nonnative-encoded.txt', mode='wb') as f:
    # Записать выбранный маркер порядка следования байтов. Он
    # не включается в кодируемый текст, поскольку порядок
    # следования байтов бьш задан явно при выборе кодировки.
    f.write(bom)
    # Записать байтовую строку кодированного текста
    f.write(encoded_text)
