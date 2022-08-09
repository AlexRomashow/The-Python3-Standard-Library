from xmlrpc.server import SimpleXMLRPCServer
import logging
import os

# Включить протоколирование операций
logging.basicConfig(level=logging.INFO)

server = SimpleXMLRPServer(
    ('localhost', 9000),
    logRequests=True,
)

# Предоставить функцию
def list_contents(dir_name):
    logging.info('list_contents(%s)', dir_name)
    return os.listdir(dir_name)

server.register_function(list_contents)

# Запустить сервер
try:
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')











