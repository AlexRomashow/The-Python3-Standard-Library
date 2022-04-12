import re

address = re.compile(
    '''
    # Имя состоит из букв и может включать символы точки '.'
    # в сокращенных вариантах обращения и инициалах
    ((?P<name>
        ([\w.,]+\s+)*[\w.,]+
        )
        \s+
    ) # Имя уже не является необязательным

    # ПРОСМОТР ВПЕРЕД
    # Адреса электронной почты заключены в угловые скобки, но
    # только в том случае, если имеются обе скобки
    # или ни одной
    (?= (<.*>$)             # Остаток заключен в угловые скобки
        |
        ([^<].*[^>]$)       # Остаток *не* заключен в угловые скобки
    )

    <? # Необязательная открывающая угловая скобка

    # Собственно электронный адрес: username@domain.tld
    (?P<email>
        [\w\d.+-]+ # Имя пользователя
        @
        ([\w\d.]+\.)+ # Префикс имени домена
        (com|org|edu) # Ограничение списка доменов верхнего уровня
    )

    >? # Необязательная закрывающая угловая скобка
    ''',
    re.VERBOSE)

candidates = [
    u'First Last ',
    u'No Brackets first.last@example.com',
    u'Open Bracket ',
]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print(' Name :', match.groupdict()['name'])
        print(' Email:', match.groupdict()['email'])
    else:
        print(' No match')




























