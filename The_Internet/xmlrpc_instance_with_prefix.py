from xmlrpc.server import SimpleXMLRPCServer
import os
import inspect

server = SimpleXMLRPCServer(
    ('localhost', 9000),
    logRequests=True,
)

def expose(f):
    "Декоратор для установки флага функции."
    f.exposed = True
    return f

def is_exposed(f):
    "Проверяет, должна ли другая функция предоставляться открыто."
    return getattr(f, 'exposed', False)

class MyService:
    PREFIX = 'prefix'

    def _dispatch(self, method, params):
        # Удалить префикс из имени метода
        if not method.startswith(self.PREFIX + '.'):
            raise Exception(
                'method "{}" is not supported'.format(method)
            )
        method_name = method.partition('.')[2]
        func = getattr(self, method_name)
        if not is_exposed(func):
            raise Exception(
                'method "{}" is not supported'.format(method)
            )
        return func(*params)

@expose
def public(self):
    return 'This is public'

def private(self):
    return 'This is private'

server.register_instance(MyService())

try:
    print('Use Control-C to exit')
    server.serve_forever()
except Keyboardinterrupt:
    print('Exiting')
