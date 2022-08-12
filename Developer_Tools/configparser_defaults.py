import configparser

# Определить имена параметров
option_names = [
    'from-default',
    'from-section', 'section-only',
    'file-only', 'init-only', 'init-and-file',
    'from-vars',
]

# Инициализировать анализатор рядом значений по умолчанию
DEFAULTS = {
    'from-default': 'value from defaults passed to init',
    'init-only': 'value from defaults passed to init',
    'init-and-file': 'value from defaults passed to init',
    'from-section': 'value from defaults passed to init',
    'from-vars': 'value from defaults passed to init',
}
parser = configparser.ConfigParser(defaults=DEFAULTS)

print('Defaults before loading file:')
defaults = parser.defaults()
for name in option_names:
    if name in defaults:
        print('{:<15} = {!r}'.format(name, defaults[name]))

# Загрузить конфигурационный файл
parser.read('with-defaults.ini')

print('\nDefaults after loading file:')
defaults = parser.defaults()
for name in option_names:
    if name in defaults:
        print('{:<15} = {!r}'.format(name, defaults[name]))

# Задать ряд локальных переопределений
vars = {'from-vars': 'value from vars'}

# Отобразить значения всех параметров
print('\nOption lookup:')
for name in option_names:
    value = parser.get('sect', name, vars=vars)
    print('{:<15} = {!r}'.format(name, value))

# Отобразить сообщения об ошибках для несуществующих параметров
print('\nError cases:')
try:
    print('No such option:', parser.get('sect', 'no-option'))
except configparser.NoOptionError as err:
    print(err)

try:
    print('No such section:', parser.get('no-sect', 'no-option'))
except configparser.NoSectionError as err:
    print(err)
