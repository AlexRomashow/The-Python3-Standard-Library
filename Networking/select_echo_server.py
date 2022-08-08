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
server.listen(5)

# Сокеты, из которых ожидается чтение данных
inputs = [server]

# Сокеты, в которые предполагается записывать данные
outputs = []

# Очереди исходящих сообщений (socket:Queue)
message_queues = {}

while inputs:
    # Ждать, пока по крайней мере один из сокетов
    # не будет готов к обработке
    print('waiting for the next event', file=sys.stderr)
    readable, writable, exceptional = select.select(inputs,
                                                    outputs,
                                                    inputs)

    # Обработать входные данные
    for s in readable:
        if s is server:
            # Читаемый сокет готов к принятию соединения
            connection, client_address = s.accept()
            print('connection from', client_address, file=sys.stderr)
            connection.setblocking(0)
            inputs.append(connection)

            # Предоставить соединению очередь для
            # буферизации отправляемых данных
            message_queues[connection] = queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                # Читаемый клиентский сокет имеет данные для
                # чтения
                print('received {!r} from {}'.format(
                    data, s.getpeername()), file=sys.stderr,
                )
                message_queues[s].put(data)
                # Добавить выходной канал для отправки ответа
                if s not in outputs:
                    outputs.append(s)
                else:
                    # Интерпретировать пустой результат как закрытие
                    # соединения
                    print('closing', client_address, file=sys.stderr)
                    # Прекратить прослушивание входного канала для
                    # данного соединения
                    if s in outputs:
                        outputs.remove(s)
                    inputs.remove(s)
                    s.close()

                    # Удалить очередь сообщений
                    del message_queues[s]

    # Обработать выходные данные
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            # Ввиду отсутствия сообщений, ожидающих обработки,
            # прекратить проверку возможности выполнения записи
            print(' ', s.getpeername(), 'queue empty',
                file=sys.stderr)
            outputs.remove(s)
        else:
            print('sending {!r} to {}'.format(next_msg,
                                        s.getpeername()),
                file=sys.stderr)
            s.send(next_msg)

    # Обработать "исключительные условия"
    for s in exceptional:
        print('exception condition on', s.getpeername(),
            file=sys.stderr)
        # Прекратить прослушивание входного канала для
        # данного соединения
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        
        # Удалить очередь сообщений
        del message_queues[s]
