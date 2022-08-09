import smtplib
import email.utils
from email.mime.text import MIMEText

# Создать сообщение
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient',
                                    'recipient@example.com'))
msg['From'] = email.utils.formataddr(('Author',
                                    'author@example.com'))
msg['Subject'] = 'Simple test message'

server = smtplib.SMTP('localhost', 1025)
server.set_debuglevel(True) # отображать информацию
                            # о подключении к серверу

try:
    server.sendmail('author@example.com',
                    ['recipient@example .com'],
                    msg.as_string())
finally:
    server.quit()

