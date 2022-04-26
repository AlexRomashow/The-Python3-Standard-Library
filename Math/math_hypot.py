import math

print('{:^7} {:^7} {:^10}'.format('X', 'Y', 'Hypotenuse'))
print('{:—^7} {:-^7} {:-^10}'.format("", "", ""))

POINTS = [
    # простые точки
    (1, 1),
    (-1, -1),
    (math.sqrt(2), math.sqrt(2)),
    (3, 4), # треугольник со сторонами 3-4-5
    # для точки окружности
    (math.sqrt(2) / 2, math.sqrt(2) / 2), # pi/4 радиана
    (0.5, math.sqrt(3) / 2), # pi/3 радиана
]

for x, у in POINTS:
    h = math.hypot(x, у)
    print('{:7.2f} {:7.2f} {:7.2f}'.format(x, у, h))
