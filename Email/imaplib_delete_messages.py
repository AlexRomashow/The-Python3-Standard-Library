import imaplib
import imaplib_connect
from imaplib_list_parse import parse_list_response

with imaplib_connect.open_connection() as c:
    c.select('Example.Today')

    # Каковы идентификаторы сообщений в почтовом ящике?
    typ, [msg_ids] = c.search(None, 'ALL')
    print('Starting messages:', msg_ids)

    # Найти сообщение (сообщения)
    typ, [msg_ids] = c.search(
        None,
        '(SUBJECT "subject goes here")',
    )
    msg_ids = ','.join(msg_ids.decode('utf-8').split(' '))
    print('Matching messages:', msg_ids)

    # Каково текущее состояние флагов?
    typ, response = c.fetch(msg_ids, '(FLAGS)')
    print('Flags before:', response)

    # Изменить флаг Deleted
    typ, response = c.store(msg_ids, '+FLAGS', r'(\Deleted)')

    # Каким стало состояние флагов?
    typ, response = c.fetch(msg_ids, '(FLAGS)')
    print('Flags after:', response)

    # Удалить сообщение навсегда
    typ, response = c.expunge()
    print('Expunged:', response)

    # Каковы идентификаторы сообщений,
    # оставшихся в почтовом ящике?
    typ, [msg_ids] = c.search(None, 'ALL')
    print('Remaining messages:', msg_ids)
