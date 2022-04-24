import decimal

# Установка контекста c ограниченной точностью
c = decimal.getcontext().copy()
c.prec = 3

# Создание собственной константы
pi = c.create_decimal('3.1415')

# Округление постоянного значения
print('PI :', pi)

# Результат использования константы c учетом
# глобального контекста
print('RESULT:', decimal.Decimal('2.01') * pi)
