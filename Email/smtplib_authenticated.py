import smtplib
import email.utils
from email.mime.text import MIMEText
import getpass

# Вывести приглашение для ввода
# информации о соединении
to_email = input('Recipient: ')
servename = input('Mail server name: ')
serverport = input('Server post: ')
if serverport:
    serverport = int(serverport)
else:
    serverport = 25
use_tls = input('Use TLS? (yes/no): ').lower()
username = input('Mail username: ')
password = getpass.getpass("%s's password: " % username)

# Создать сообщение
msg = MIMEText('Test message from PyMOTW.')
msg.set_unixfrom('author')
msg['To'] = email.utils.formataddr(('Recipient', to_email))
msg['From'] = email.utils.formataddr(('Author', 'author@example.com'))
msg['Subjec'] =  'Test from PyMOTW'

if use_tls == 'yes':
    print('starting with a secure connection')
    server = smtplib.SMTP_SSL(servername, serverport)
else:
    print('starting with an insecure connection')
    server = smtplib.SMTP(servername, serverport)
try:
    server.set_debuglevel(True)
    
    # Идентифицировать себя, запрашивая информацию о
    # поддерживаемых средствах
    server.ehlo()

    # Использовать шифрование в этой сессии, если оно поддерживается
    if server.has_extn('STARTTLS'):
        print('(starting TLS)')
        server.starttls ()
        server.ehlo()   # повторно идентифицировать себя
                        # посредством TLS-соединения
    else:
        print('(no STARTTLS)')

    if server.has_extn('AUTH'):
        print('(logging in)')
        server.login(username, password)
    else:
        print('(no AUTH)')

server.sendmail('author@example.com',
                [to_email],
                msg.as_string())
finally:
    server.quit()

