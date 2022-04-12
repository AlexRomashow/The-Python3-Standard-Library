import re 

address = re.compile(
    r'''
    # ФИО в обычной форме
    (\w+)          # Имя
    \s+
    (([\w.]+)\s+)? # Необязательное отчество или инициалы
    (\w+)          # Фамилия

    \s+

    <
    # Адрес: имя.фамилия@domain.tld
    (?P<email>
        \1         # Имя
        \.
        \4         # Фамилия
        @
        ([\w\d.]+\.)+ # Префикс имени домена
        (com|org|edu) # Ограничение доменов верхнего уровня
    )

    >
    ''',
    re.VERBOSE | re.IGNORECASE)

candidates = [
    u'First Last <first.last@example.com>',
    u'Different Name <first.last@example.com>',
    u'First Middle Last <first.last@example.com >',
    u'First M. Last <first.last@example.com >',
    ]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print(' Match name :', match.group(1), match.group(4))
        print(' Match email:', match.group(5))
    else:
        print(' No match')
    
