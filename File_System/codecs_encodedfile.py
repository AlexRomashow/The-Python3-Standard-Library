from codecs_to_hex import to_hex

import codecs
import io

# "Сырая" версия исходных данных
data = 'français'

# Кодирование вручную c использованием кодировки UTF-8
utf8 = data.encode('utf-8')
print('Start as UTF-8:', to_hex(utf8, 1))

# Задание выходного буфера и обертывание его
# классом EncodedFile
output = io.BytesIO()
encoded_file = codecs.EncodedFile(output, data_encoding='utf-8',
                                    file_encoding='utf-16')
encoded_file.write(utf8)

# Извлечение содержимого буфера в виде байтовой
# строки в кодировке UTF-16
utf16 = output.getvalue()
print('Encoded to UTF-16:', to_hex(utf16, 2))

# Задание другого буфера для чтения данных UTF-16
# и обертывание его другим классом EncodedFile
buffer = io.BytesIO(utf16)
encoded_file = codecs.EncodedFile(buffer, data_encoding='utf-8',
                                    file_encoding='utf-16')

# Чтение версии данных в кодировке UTF-8
recoded = encoded_file.read()
print('Back to UTF-8:', to_hex(recoded, 1))
