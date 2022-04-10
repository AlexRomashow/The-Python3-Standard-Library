import re

def text_patterns(text, patterns):
    """Получив исходный текст и список шаблонов в качестве
    аргументов, выполняет поиск всех вхождений каждого шаблона
    в тексте и направляет результаты в стандартный поток вывода
    stdout.
    """
    # Поиск всех вхождений шаблона в тексте и вывод результатов
    for pattern, desc in patterns:
        print(f"'{pattern}' ({desc})\n")
        print(f" '{text}' ")
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)
            print(f" {prefix}'{substr}'")
        print()
    return 

if __name__ == "__main__":
    text_patterns('abbaaabbbbaaaaa', [('ab', "'a' followed by 'b'"),])
