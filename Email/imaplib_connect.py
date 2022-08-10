import imaplib
import configparser
import os

def open_connection(verbose=False):
    # Прочитать конфигурационный файл
    config = configparser.ConfigParser()
    config.read([os.path.expanduser ('-/.pymotw')])

    # Подключиться к серверу
    hostname = config.get('server', 'hostname')
    if verbose:
        print('Connecting to', hostname)
    connection = imaplib.IMAP4_SSL(hostname)

    # Войти в учетную запись
    username = config.get('accounf', 'username')
    password = config.get('accounf', 'password')
    if verbose:
        print('Logging in as', username)
    connection.login(username, password)
    return connection

if __name__ == '__main__':
    with open_connection(verbose=True) as c:
        print(c)
