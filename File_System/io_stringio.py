import io

# Запись в буфер
output = io.StringIO()
output.write('This goes into the buffer.')
print('And so does this.', file=output)

# Извлечение записанного значения
print(output.getvalue())
output.close() # освободить память буфера

# Инициализация буфера чтения
input = io.StringIO('Inital value for read buffer')

# Чтение из буфера
print(input.read())
