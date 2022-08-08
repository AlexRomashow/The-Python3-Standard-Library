import threading
import socketserver

class ThreadedEchoRequestHandler(socketserver.BaseRequestHandler):
    
    def handler(self):
        # Эхо-сообщение клиенту
        data = self.request.recv(1024)
        cur_thread = threading.currentThread()
        response = b'%s: %s' % (cur_thread.getName().encode(), data)
        self.request.send(response)
        return

class ThreadedEchoServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == '__main__':
    import socket

    address = ('localhost', 0) # позволить ядру назначить порт
    server = ThreadedEchoServer(address, ThreadedEchoRequestHandler)
    ip, port = server.server_address # Какой порт назначен?

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True) # работать в фоновом режиме
    t.start()
    print('Server loop running in thread:', t.getName())

    # Подключиться к серверу
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Отправить данные
    message = b'Hello, world'
    print('Sending : {!r}'.format(message))
    len_sent = s.send(message)

    # Получить ответ
    response = s.recv(1024)
    print('Received: {!r}'.format(response))

    # Очистить ресурсы
    server.shutdown()
    s.close()
    server.socket.close()
