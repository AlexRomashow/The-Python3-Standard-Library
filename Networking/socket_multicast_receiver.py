import socket
import struct
import sys

multicast_group = '224.3.29.71'

server_address = ('', 10000)

# Создать сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Привязать сокет к адресу сервера
sock.bind(server_address)

# Приказать операционной системе добавить сокет в
# мультикастную группу на всех интерфейсах
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_ADD_MEMBERSHIP,
    mreq)

# Цикл получения сообщений и отправки ответов
while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(1024)

    print('received {} bytes from {}'.format(len(data), address))
    print(data)

    print('sending acknowledgement to', address)
    sock.sendto(b'ack', address)
