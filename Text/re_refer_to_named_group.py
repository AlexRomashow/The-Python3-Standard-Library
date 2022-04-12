import re

address = re.compile(
    '''
    # ФИО в обычной форме
    (?P<first_name>\w+)
    \s+
    (([\w.]+)\s+)? # Необязательное отчество или инициалы
    (?P<last_name>\w+)
    \s+
    <
    # Адрес: имя.фамилия@domain.tld
    (?P<email>
        (?P=first_name)
        \.
        (?P=last_name)
        @
        ([\w\d.]+\.)+ # Префикс домена верхнего уровня
        (com|org|edu) # Ограничение доменов верхнего уровня
    )
    >
    ''',
    re.VERBOSE | re.IGNORECASE)

candidates = [
    u'First Last <first.last@example.com>',
    u'Different Name <first.last@example.com>',
    u'First Middle Last <first.last@example.com>',
    u'First M. Last <first.last@example.com>',
    ]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print(' Match name :', match.groupdict()['first_name'], end=' ')
        print(match.groupdict()['last_name'])
        print(' Match email:', match.groupdict()['email'])
    else:
        print(' No match')
