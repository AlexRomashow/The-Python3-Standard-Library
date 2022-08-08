import select
import socket
import sys
import queue

# Создать сокет TCP/IP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# Привязать сокет к порту
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address), file=sys.stderr)
server.bind(server_address)

# Слушать входящие соединения
server.listen (5)

# Очереди исходящих сообщений
message_queues = {}

# Предотвратить бесконечное блокирование(миллисекунды)
TIMEOUT = 1000

# Обычно используемые установки флагов
READ_ONLY = (
    select.POLLIN |
    select.POLLPRI |
    select.POLLHUP |
    select.POLLERR
)
READ_WRITE = READ_ONLY | select.POLLOUT

# Зарегистрировать объект, выполняющий опрос
poller = select.poll()
poller.register(server, READ_ONLY)

# Сопоставить дескрипторы файлов c объектами сокетов
fd_to_socket = {
    server.fileno(): server,
}

while True:
    # Ждать, пока по крайней мере один из сокетов не перейдет
    # в состояние готовности к выполнению обработки
    print('waiting for the next event', file=sys.stderr)
    events = poller.poll(TIMEOUT)

    for fd, flag in events:
        # Получить фактический сокет по его дескриптору файла
        s = fd_to_socket[fd]
        # Обработать входные данные
        if flag & (select.POLLIN | select.POLLPRI):
            if s is server:
                # Читаемый сокет готов принять соединение
                connection, client_address = s.accept()
                print('connection', client_address,
                    file=sys.stderr)
                connection.setblocking(O)
                fd_to_socket[connection.fileno()] = connection
                poller.register(connection, READ_ONLY)

                # Предоставить соединению очередь для буферизации
                # отправляемых данных
                message_queues[connection] = queue.Queue()
            else:
                data = s.recv(1024)
                if data:
                    # Читаемый клиентский сокет имеет данные для чтения
                    print('received {!r} from {}'.format(
                        data, s.getpeername()), file=sys.stderr,
                    )
                    message_queues[s].put(data)
                    # Добавить выходной канал для отправки ответа
                    poller.modify(s, READ_WRITE)
                else:
                    # Интерпретировать пустой результат как
                    # закрытие соединения
                    print('closing', client_address,
                        file=sys.stderr)
                    # Прекратить прослушивание входных данных
                    # для этого соединения
                    poller.unregister(s)
                    s.close()

                    # Удалить очередь сообщений
                    del message_queues[s]
        elif flag & select.POLLHUP:
            # Клиент отключился
            print('closing', client_address, '(HUP)',
                file=sys.stderr)
            # Прекратить прослушивание входных данных
            # для этого соединения
            poller.unregister(s)
            s.close()
        elif flag & select.POLLOUT:
            # Сокет готов к отправке данных,
            # если таковые имеются
            try:
                next_msg = message_queues[s].get__nowait()
            except queue.Empty:
                # Ввиду отсутствия сообщений, ожидающих
                # обработки, прекратить проверку готовности
                # сокета к выполнению записи
                print(s.getpeername(), 'queue empty',
                    file=sys.stderr)
                poller.modify(s, READ_ONLY)
            else:
                print('sending {!r} to {}'.format(
                    next_msg, s.getpeername()), file=sys.stderr,
                )
                s. send(next_msg)
        elif flag & select.POLLERR:
            print('exception on', s.getpeername(),
                file=sys.stderr)
            # Прекратить прослушивание входных данных для
            # этого соединения
            poller.unregister(s)
            s.close()
            
            # Удалить очередь сообщений
            del message_queues[s]
