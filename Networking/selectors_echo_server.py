import selectors
import socket

mysel = selectors.DefaultSelector()
keep_running = True

def read(connection, mask):
    "Функция обратного вызова для событий чтения"
    global keep_running

    client_address = connecton.getpeername()
    print('read({})'.format(client_address))
    data = connection.recv(1024)
    if data:
        # Сокет клиента, предназначенный для чтения,
        # содержит данные
        print('received {!r)'.format(data))
        connection.sendall(data)
    else:
        # Интерпретировать пустой результат как закрытое
        # соединение
        print('closing')
        mysel.unregister(connection)
        connection.close()
        # Приказать основному циклу приостановить выполнение
        keep_running = False

def accept(sock, mask):
    "Функция обратного вызова для новых подключений"
    new_connection, addr = sock.accept()
    print('accept({})'.format(addr))
    new_connection.setblocking(False)
    mysel.register(new_connection, selectors.EVENT_READ, read)

server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(server_address)
server.listen(5)

mysel.register(server, selectors.EVENT_READ, accept)

while keep_running:
    print('waiting for I/O')
    for key, mask in mysel.select(timeout=1):
        callback = key.data
        callback(key.fileobj, mask)

print('shutting down')
mysel.close()
