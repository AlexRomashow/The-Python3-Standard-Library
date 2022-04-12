import re

address = re.compile(
    '''
    # Имя состоит из букв и может включать символы точки "."
    # в сокращенных вариантах обращения и инициалах
    ((?P<name>
       ([\w.,]+\s+)*[\w.,]+)
       \s*
       # Адреса электронной почты заключаются в угловые скобки
       # < >, но только если найдено имя, поэтому открывающая
       # угловая скобка включена в эту группу
       <
    )? # Полное имя является необязательным элементом

    # Собственно электронный адрес: username@domain.tld
    (?P<email>
      [\w\d.+-]+       # Имя пользователя
      @
      ([\w\d.]+\.)+    # Префикс имени домена
      (com|org|edu)    # Ограничение списка доменов верхнего уровня
    )

    >? # Необязательная закрывающая угловая скобка
    ''',
    re.VERBOSE)

candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valid@example.foo',
    u'First Last ',
    u'No Brackets first.last@example.com',
    u'First Last',
    u'First Middle Last ',
    u'First M. Last ',
    u'',
]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print(' Name:', match.groupdict()['name'])
        print(' Email:', match.groupdict()['email'])
    else:
        print(' No match')









