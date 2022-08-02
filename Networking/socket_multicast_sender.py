import socket
import struct
import sys

message = b'very important data'
multicast_group = ('224.3.29.71', 10000)

# Создать сокет для датаграмм
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Задать тайм-аут, чтобы избежать бесконечной блокировки сокета
# при попытках получения данных
sock.settimeout(0.2)

# Установить для сообщений значение ttl, равное 1, чтобы
# они не выходили за пределы сегмента локальной сети
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:
    # Послать данные мультикастной группе
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, multicast_group)

    # Ожидать ответы от всех получателей
    while True:
        print('waiting to receive')
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print('timed out, no more responses')
            break
        else:
            print('received {!r} from {}'.format(data, server))

finally:
    print('closing socket')
    sock.close()
