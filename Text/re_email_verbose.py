import re

address = re.compile(
    '''
    [\w\d.+-]+ # Имя пользователя
    @
    ([\w\d.]+\.)+    # Префикс имени домена
    (com|org|edu)    # TODO: поддержка других доменов верхнего уровня
    ''',
    re.VERBOSE)

candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valid@example.foo',
    ]

for candidate in candidates:
    match = address.search(candidate)
    print('{:<30} {}'.format(candidate, 'Matches' if match else 'No match'),)
