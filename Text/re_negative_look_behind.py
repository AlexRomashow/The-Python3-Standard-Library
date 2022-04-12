import re

address = re.compile(
    '''
    ^
    # Адрес: username@domain.tld
    [\w\d.+-]+ # Имя пользователя
    # Игнорировать адреса noreply
    (?<!noreply)
    @
    ([\w\d.]+\.)+ # Префикс имени домена
    (com|org|edu) # Ограничение списка доменов верхнего уровня
    $
    ''',
    re.VERBOSE)

candidates = [
    u'first.last@example.com',
    u'noreply@example.com',
    ]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print(' Match:', candidate[match.start():match.end()])
    else:
        print(' No match')
