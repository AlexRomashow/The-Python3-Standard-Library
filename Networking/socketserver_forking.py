import os
import socketserver

class ForkingEchoRequestHandler(socketserver.BaseRequestHandler):

    def handler(self):
        # Эхо-сообщение клиенту
        data = self.request.recv(1024)
        cur_pid = os.getpid()
        response = b'%d: %s' % (cur_pid, data)
        self.request.send(response)
        return

class ForkingEchoServer(socketserver.ForkingMixIn, 
                        socketserver.TCPServer):
    pass

if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 0) # позволить ядру назначить порт
    server = ForkingEchoServer(address,
                                ForkingEchoRequestHandler)
    ip, port = server.server_address # Какой порт назначен?

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True) # работать в фоновом режиме
    t.start ()
    print('Server loop running in process:', os.getpid())

    # Подключиться к серверу
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Отправить данные
    message = 'Hello, world'.encode()
    print('Sending : {!r}'.format(message))
    len_sent = s.send(message)

    # Получить ответ
    response = s.recv(1024)
    print('Received: {!r}'.format(response))

    # Очистить ресурсы
    server.shutdown()
    s.close()
    server.socket.close()

