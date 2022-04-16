import weakref

class ExpensiveObject:

    def __del__(self):
        print('(Deleting {})'.format(self))

def callback(reference):
    """Вызывается при удалении целевого объекта"""
    print('callback({!r})'.format(reference))

obj = ExpensiveObject()
r = weakref.ref(obj, callback)

print('obj:', obj)
print('ref:', r)
print('r():', r())

print('deleting obj')
del obj
print(r'():', r())
