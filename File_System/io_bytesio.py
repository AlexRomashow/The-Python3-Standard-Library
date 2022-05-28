import io

# Запись в буфер
output = io.BytesIO()
output.write('This goes into the buffer,'.encode('utf-8'))
output.write('AQE'.encode('utf-8'))

# Извлечение записанного значения
print(output.getvalue())
output.close() # освободить память буфера

# Инициализация буфера чтения
input = io.BytesIO(b'Inital value for read buffer')

# Чтение из буфера
print(input.read())
