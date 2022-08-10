import imaplib
import imaplib_connect

with imaplib_connect.open_connection() as c:
    # Найти сообщения c флагом "SEEN" в папке INBOX
    c.select('INBOX')
    typ, [response] = c.search(None, 'SEEN')
    if typ != 'OK':
        raise RuntimeError(response)
    msg_ids = ','.join(response.decode('utf-8').split(' '))

    # Создать новый почтовый ящик "Example.Today"
    typ, create_response = c.create('Example.Today')
    print('CREATED Example.Today:', create_response)

    # Копировать сообщения
    print('COPYING:', msg_ids)
    c.copy(msg_ids, 'Example.Today')

    # Просмотреть результаты
    c.select('Example.Today')
    typ, [response] = c.search(None, 'ALL')
    print('COPIED:', response)
