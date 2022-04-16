import functools

def myfunc(a, b=2):
    "Docstring for myfunc()."
    print('called myfunc with:', (a, b))

def show_details(name, f, is_partial=False):
    "Показать детали вызываемого объекта."
    print('{}:'.format(name))
    print('object:', f)
    if not is_partial:
        print('__name__:', f.__name__)
    if is_partial:
        print('func:', f.func)
        print('args:', f.args)
        print('keywords:', f.keywords)
    return

show_details('myfunc', myfunc)
myfunc('a', 3)
print()

# Задать другое значение по умолчанию для 'b', но потребовать,
# чтобы вызывающий код предоставил 'a'

p1 = functools.partial(myfunc, b=4)
show_details('partial with named default', p1, True)
p1('passing a')
p1('override b', b=5)
print()

# Задать значения по умолчанию для 'a' и 'b'
p2 = functools.partial(myfunc, 'default a', b=99)
show_details('partial with defaults', p2, True)
p2()
p2(b='override b')
print()
print('Insufficient argumetns:')
p1()








