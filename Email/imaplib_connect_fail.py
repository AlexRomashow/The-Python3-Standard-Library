import imaplib
import configparser
import os

def open_connection(verbose=False):
    # Прочитать конфигурационный файл
    config = configparser.ConfigParser()
    config.read([os.path.expanduser ('-/.pymotw')])

    # Подключиться к серверу
    hostname = config.get('server', 'hostname')
    print('Connecting to', hostname)
    connection = imaplib.IMAP4_SSL(hostname)

    # Войти в учетную запись
    username = config.get('accounf', 'username')
    password = 'this_is_the_wrong_password'
    print('Logging in as', username)
try:
    connection.login(username, password)
except Exception as err:
    print('ERROR:', err)
