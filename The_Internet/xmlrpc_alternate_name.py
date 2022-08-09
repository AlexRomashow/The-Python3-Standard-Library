from xmlrpc.server import SimpleXMLRPCServer
import os

server = SimpleXMLRPCServer(('localhost', 9000))

def list_contents(dir_name):
    "Предоставляет функцию c альтернативным именем"
    return os.listdir(dir_name)

server.register_function(list_contents, 'dir')

try:
    print('User Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
