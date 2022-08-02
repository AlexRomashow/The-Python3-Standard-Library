import socket
import sys

def get_constants(prefix):
    """Создать словарь, сопоставляющий константы
    модуля socket c их именами.
    """
    return {
            getattr(socket, n): n
            for n in dir(socket)
            if n.startswith(prefix)
    }
families = get_constants('AF_')
types = get_constants('SOCK')
protocols = get_constants('IPPROTO_')

# Создать сокет TCP/IP
sock = socket.create_connection(('localhost', 10000))

print('Family  :', families[sock.family])
print('Type    :', types[sock.type])
print('Protocol:', protocols[sock.proto])
print()

try:
    # Отправить данные
    message = b'This is message. It will be repeated.'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()

