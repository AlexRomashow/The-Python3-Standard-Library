import sys
import socketserver

class Echo(socketserver.BaseRequestHandler) :
    def handle(self):
        """Получить байты и вернуть их клиенту.
        Декодировать данные не нужно, поскольку они не
        используются.
        """
        data = self.request.recv(1024)
        self.request.send(data)

class PassThrough:
    
    def __init__(self, other):
        self.other = other

    def write(self, data):
        print('Writing :', repr(data))
        return self.other.write(data)

    def read(self, size=-1):
        print('Reading :', end=' ')
        data = self.other.read(size)
        print(repr(data))
        return data

    def flush(self):
        return self.other.flush()

    def close(self):
        return self.other.close()

if __name__ == '__main__':
    import codecs
    import socket
    import threading

    address = ('localhost', 0)
    # позволить ядру назначить порт
    server = socketserver.TCPServer(address, Echo)
    ip, port = server.server_address # Какой порт назначен?

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True) # превратить поток в поток-демон
    t.start()
    
    # Подключение к серверу
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    
    # Обертывание сокета объектом чтения или записи
    read_file = s.makefile('rb')
    incoming = codecs.getreader('utf-8')(PassThrough(read_file))
    write_file = s.makefile('wb')
    outgoing = codecs.getwriter('utf-8')(PassThrough(write_file))

    # Отправка данных
    text = 'français'
    print('Sending :', repr(text))
    outgoing.write(text)
    outgoing.flush()
    
    # Получение ответа
    response = incoming.read()
    print('Received:', repr(response))

    # Освобождение ресурсов
    s.close()
    server.socket.close()

