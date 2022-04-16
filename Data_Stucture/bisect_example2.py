import bisect
# Последовательность случайных чисел
values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('New Pos Contents')
print('--- --- --------')

# Используются функции bisect_left() и insort_left()
l = []
for i in values:
    position = bisect.bisect_left(l, i)
    bisect.insort_left(l, i)
    print('{:3} {:3}'.format(i, position), l)
