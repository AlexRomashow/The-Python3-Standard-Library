from configparser import ConfigParser
import codecs

parser = ConfigParser()
# Открыть файл, используя корректную кодировку
parser.read('unicode.ini', encoding='utf-8')

password = parser.get('bug_tracker', 'password')

print('Password:', password.encode('utf-8'))
print('Type    :', type(password))
print('repr()  :', repr(password))
