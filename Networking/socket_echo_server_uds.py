import socket
import sys
import os

server_address = './uds_socket'

# Убедиться в том, что сокет еще не существует
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

# Создать сокет UDS
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Привязать сокет к адресу
print('starting up on {}'.format(server_address))
sock.bind(server_address)

# Слушать входящие соединения
sock.listen(1)

while True:
    # Ждать соединения
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        # Получать данные небольшими порциями и
        # отправлять их обратно
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        # Закрыть соединение
        connection.close()
