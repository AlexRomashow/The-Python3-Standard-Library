import cgi
from http.server import BaseHTTPRequestHandler
import io

class PostHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # Анализ выгруженных данных
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': self.headers['Content-Type'],
            }
        )

        # Начать отвечать
        self.send_response(200)
        self.send_header('Content-Type',
                        'text/plain; charset=utf-8')
        self.end_headers()

        out = io.TextIOWrapper(
            self.wfile,
            encoding='utf-8',
            line_buffering=False,
            write_through=True,
        )

        out.write('Client: {}\n'.format(self.client_address))
        out.write('User-agent: {}\n'.format(
            self.headers['user-agent']))
        out.write('Path: {}\n'.format(self.path))
        out.write('Form data:\n')

        # Отправляемая обратно клиенту информация о данных,
        # выгруженных на сервер вместе c формой
        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                # Это поле содержит выгруженный файл
                file_data = field_item.file.read()
                file_len = len(file_data)
                del file_data
                out.write(
                    '\nUploaded {} as {!r} ({} bytes)\n'.format(
                        field, field_item.filename, file_len)
                )
            else:
                # Обычное значение формы
                out.write('\t{}={}\n'.format(
                    field, form[field].value))
        
        # Отключить экземпляр TextIOWrapper от базового буфера,
        # чтобы его удаление не привело к закрытию сокета, который
        # по-прежнему используется сервером
        out.detach()

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), PostHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()



















