import io

# Запись в буфер
output = io.BytesIO()
wrapper = io.TextIOWrapper(
                output,
                encoding='utf-8',
                write_through=True,
)
wrapper.write('This goes into the buffer.')
wrapper.write('AQE')

# Извлечение записанного значения
print(output.getvalue())

output.close() # освободить память буфера

# Инициализация буфера чтения
input = io.BytesIO(
    b'Inital value for read buffer with unicode characters ' +
    'AQE'.encode('utf-8')
)
wrapper = io.TextIOWrapper(input, encoding='utf-8')

# Чтение из буфера
print(wrapper.read())
