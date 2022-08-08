from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import Binary
import datetime

class ExampleService:
    def ping(self):
        """Простая функция, срабатывающая при вызове
        для демонстрации подключения.
        """
        return True

    def now(self):
        """возвращает текущие дату и время сервера."""
        return datetime.datetime.now()

    def show_type(self, arg):
        """Иллюстрирует передачу типов в серверные методы.
        Получает один аргумент любого типа.
        Возвращает кортеж со строковым представлением значения,
        имя типа и само значение.
        """
        return (str(arg), str(type(arg)), arg)

    def raises_exception(self, msg):
        """Всегда возбуждает исключение RuntimeError c переданным
        сообщением."""
        raise RuntimeError(msg)

    def send_back_binary(self, bin):
        """Получает один двоичный аргумент, который распаковывается
        и перепаковывается для возврата."""
        data = bin.data
        print ('send__back_binary({!r})'. format(data))
        response = Binary(data)
        return response

if __name__ == "__main__":
    server = SimpleXMLRPCServer(('localhost', 9000),
                                logRequests=True,
                                allow_none=True)
    server.register_introspection_functions()
    server.register_multicall_functions()
    server.register_instance(ExampleService())
    try:
        print('Use Control-C to exit')
        server.serve_forever()
    except Keyboardinterrupt:
        print('Exiting')

