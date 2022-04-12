import re

address = re.compile(
    '''
    ^
    # Имя состоит из букв и может включать символы точки "."
    # в сокращенных вариантах обращения и инициалах
    (?P<name>
        ([\w.]+\s+)*[\w.]+
    )?
    \s*

    # Адреса электронной почты должны быть заключены в угловые
    # скобки, но только в том случае, если найдено имя
    (?(name)
    # Остаток заключен в угловые скобки, поскольку
    # имя присутствует
    (?P<brackets>(?=(<.*>$)))
    |
    # Остаток не заключен в угловые скобки, поскольку
    # имя отсутствует
    (?=([^<].*[^>]$))
    )
    
    # Находить угловую скобку только в том случае, если
    # опережающая проверка обнаружила обе скобки
    (?(brackets)<|\s*)

    # Собственно адрес: username@domain.tld
    (?P<email>
        [\w\d.+-]+ # Имя пользователя
        @
        ([\w\d.]+\.)+ # Префикс имени домена
        (com|org|edu) # Ограничение списка доменов верхнего уровня
    )
    # Находить угловую скобку только в том случае, если
    # опережающая проверка обнаружила обе скобки
    (?(brackets)>|\s*)
    $
    ''',
    re.VERBOSE)

candidates = [
    u'First Last <first.last@example.com>',
    u'No Brackets first.last@example.com',
    u'Open Bracket <first.last@example.com',
    u'Close Bracket first.last@example.com>',
    u'no.brackets@example.com'
    ]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print(' Match name :', match.groupdict()['name'])
        print(' Match email:', match.groupdict()['email'])
    else:
        print(' No match')




