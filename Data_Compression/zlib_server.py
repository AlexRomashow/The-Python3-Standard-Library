import zlib
import logging
import socketserver
import binascii

BLOCK_SIZE = 64

class ZlibRequestHandler(socketserver.BaseRequestHandler):

    logger = logging.getLogger('Server')

    def handle(self):
        compressor = zlib.compressobj(1)

        # Определение файла, запрашиваемого клиентом
        filename = self.request.recv(1024).decode('utf-8')
        self.logger.debug('client asked for: %r', filename)

        # Отправка порций данных по мере их сжатия
        with open(filename, 'rb') as input:
            while True:
                block = input.read(BLOCK_SIZE)
                if not block:
                    break
                self.logger.debug('RAW %r', block)
                compressed = compressor.compress(block)
                if compressed:
                    self.logger.debug(
                        'SENDING %r',
                        binascii.hexlify(compressed))
                else:
                    self.logger.debug('BUFFERING')

        # Отправка данных, буферизуемых упаковщиком
        remaining = compressor.flush()
        while remaining:
            to_send = remaining[:BLOCK_SIZE]
            remaining = remaining[BLOCK_SIZE:]
            self.logger.debug('FLUSHING %r',
                            binascii.hexlify(to_send))
            self.request.send(to_send)
        return 

if __name__ == '__main__':
    import socket
    import threading
    from io import BytesIO

    logging.basicConfig (
        level=logging.DEBUG,
        format='%(name)s: %(message)s',
    )
    logger = logging.getLogger('Client')

    # Настроить сервер, выполняющийся в отдельном потоке
    address = ('localhost', 0) # позволить ядру назначить noptf
    server = socketserver.TCPServer(address, ZlibRequestHandler)
    ip, port = server.server_address # Какой порт назначен?
    
    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()
    
    # Подключиться к серверу в качестве клиента
    logger.info('Contacting server on %s:%s', ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Запросить файл
    requested_file = 'lorem.txt'
    logger.debug('sending filename: %r', requested_file)
    len_sent = s.send(requested_file.encode('utf-8'))

    # Получить ответ
    buffer = BytesIO()
    decompressor = zlib.decompressobj()
    while True:
        response = s.recv(BLOCK_SIZE)
        if not response:
            break
        logger.debug('READ %r', binascii.hexlify(response))

        # Включить неиспользованные данные
        # при передаче данных распаковщику
        to_decompress = decompressor.unconsumed_tail + response
        while to_decompress:
            decompressed = decompressor.decompress(to_decompress)
            if decompressed:
                logger.debug('DECOMPRESSED %r', decompressed)
                buffer.write(decompressed)
                # Поиск данных, не использованных из-за
                # переполнения буфера
                to_decompress = decompressor.unconsumed_tail
            else:
                logger.debug('BUFFERING')
                to_decompress = None
    
    # Обработка данных, оставшихся в буфере распаковщика
    remainder = decompressor.flush()
    if remainder:
        logger.debug('FLUSHED %r', remainder)
        buffer.write(remainder)

    full_response = buffer.getvalue()
    lorem = open('lorem.txt', 'rb').read()
    logger.debug('response matches file contents: %s',
            full_response == lorem)

    # Освобождение ресурсов
    s.close()
    server.socket.close()
