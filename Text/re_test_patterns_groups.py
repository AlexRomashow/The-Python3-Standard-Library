import re

def test_patterns(text, patterns):
    """Получив исходный текст и список шаблонов в качестве
    аргументов, выполняет поиск всех вхождений каждого шаблона
    в тексте и направляет результаты в стандартный поток вывода
    stdout.
    """
    # Поиск всех вхождений шаблона в тексте и вывод результатов
    for pattern, desc in patterns:
        print('{!r} ({})\n'.format(pattern, desc))
        print(' {!r}'.format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            prefix = ' ' * s
            print(' {}{!r}{} '.format(prefix, 
                                      text[s:e],
                                      ' ' * (len(text) - 3)),
                                      end=" ",)
            print(match.groups())
            if match.groupdict():
                print('{}{}'.format(
                    ' ' * (len(text) - s),
                    match.groupdict()),)
        print()
    return 
