from xml.etree.ElementTree import (
    Element, SubElement, tostring, XML,
)
from ElementTree_pretty import prettify

top = Element('top')

parent_a = SubElement(top, 'parent', id='A')
parent_b = SubElement(top, 'parent', id='B')
# Создать дочерние узлы
children = XML(
    '<root><child num="0" /><child num="1" />'
    '<child num="2" /></root>'
)
# Установка атрибутов id со значениями id объектов узлов
# для более отчетливой демонстрации наличия дубликатов
for c in children:
    c.set('id', str(id(c)))

# Добавление узла в первый родительский узел
parent_a.extend(children)

print('A:')
print(prettify(top))
print()
# Копирование узлов во второй родительский узел
parent_b.extend(children)

print('B:')
print(prettify(top))
print()
