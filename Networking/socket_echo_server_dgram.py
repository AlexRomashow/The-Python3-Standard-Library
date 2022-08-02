import socket
import sys

# Создать сокет UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Привязать сокет к порту
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print('sent {} bytes back to {}'.format(sent, address))
