import gc
from pprint import pprint
import weakref

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

class ExpensiveObject:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'ExpensiveObject({})'.format(self.name)

    def __del__(self):
        print('(Deleting {})'.format(self))

def demo(cache_factory):
    # Удержать объекты для того, чтобы предотвратить
    # немедленное удаление слабых ссылок
    all_refs = {}
    # Создать кеш, используя функцию-фабрику
    print('CACHE TYPE:', cache_factory)
    cache = cache_factory()
    for name in ['one', 'two', 'three']:
        o = ExpensiveObject(name)
        cache[name] = o
        all_refs[name] = o
        del o # уменьшить счетчик ссылок

    print('all_refs =', end=' ')
    pprint(all_refs)
    print('\n Before, cache contains:', list(cache.keys()))
    for name, value in cache.items():
        print('{} = {}'.format(name, value))
        del value # уменьшить счетчик ссылок

    # Удалить все ссылки на объекты,
    # которые находятся в кеше
    print('\n Cleanup:')
    del all_refs
    gc.collect()

    print('Xn After, cache contains:', list(cache.keys()))
    for name, value in cache.items():
        print('{} - {}'.format(name, value))
    print('demo returning')
    return

demo(dict)
print()
demo(weakref.WeakValueDictionary)







