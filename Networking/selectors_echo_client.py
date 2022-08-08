import selectors
import socket

mysel = selectors.DefaultSelector()
keep_running = True
outgoing = [
    b'It will be repeated.',
    b'This is the message.',
    ]
bytes_sent = 0
bytes_received = 0

# Установление соединения - блокирующая операция, поэтому
# после ее выполнения следует вызвать метод setblocking()
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)
sock.setblocking(False)

# Настроить селектор для отслеживания готовности сокета к отправке
# данных, а также наличия данных для чтения
mysel.register(
    sock,
    selectors.EVENT_READ | selectors.EVENT_WRITE,
    )

while keep_running:
    print('waiting for I/O')
    for key, mask in mysel.select(timeout=1):
        connection = key.fileobj
        client_address = connection.getpeername()
        print('client({})'.format(client_address))

        if mask & selectors.EVENT_READ:
            print('ready to read')
            data = connection.recv(1024)
            if data:
                # Сокет клиента, предназначенный для чтения,
                # получил данные
                print('received {!r}'.format(data))
                bytes_received += len(data)

            # Прекратить выполнение при получении пустого
            # результата, указывающего на закрытие соединения,
            # а также после получения копии всех отправленных
            # данных
            keep_running = not (
                data or (bytes_received and (bytes_received == bytes_sent))
            )
        if mask & selectiors.EVENT_WRITE:
            print('ready to write')
            if not outgoing:
                # Сообщения отсутствуют, поэтому записывать больше
                # нечего. Изменить регистрацию, оставив только
                # чтение ответов от сервера.
                print('switching to read-only')
                mysel.modify(sock, selectors.EVENT_READ)
            else:
                # Отправить следующее сообщение
                next_msg = outgoing.pop()
                print('sending {!r}'.format(next_msg))
                sock.sendall(next_msg)
                bytes_sent += len(next_msg)

print('shutting down')
mysel.unregister(connection)
connection.close()
mysel.close()
