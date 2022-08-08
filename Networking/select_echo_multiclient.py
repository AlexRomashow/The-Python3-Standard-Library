import socket
import sys

messages = [
    'This is the message.',
    'It will be sent ',
    'in parts.',
]

server_address = ('localhost', 10000)

# Создать сокет TCP/IP
socks = [
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
]

# Подключить сокет к порту, который прослушивается сервером
print('connecting to {} port {}'.format(*server_address),
        file=sys.stderr)
for s in socks:
    s.connect(server_address)

for message in messages:
    outgoing_data = message.encode()

    # Послать сообщения в оба сокета
    for s in socks:
        print('{}: sending {!r}'.format(s.getsockname(), 
                                        outgoing_data),
                file=sys.stderr)
        s.send(outgoing_data)

    # Прочитать сообщения в обоих сокетах
    for s in socks:
        data  = s.recv(1024)
        print('{}: received {!r}'.format(s.getsockname(),
                                        data),
            file=sys.stderr)
        if not data:
            print('closing socket', s.getsockname(),
                    file=sys.stderr)
            s.close()
