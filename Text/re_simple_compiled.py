import re

# Предварительная компиляция шаблонов
regexes = [re.compile(p) for p in ['this', 'that']]
text = 'Does this text match the pattern?'

print(f'Text: {text}\n')

for regex in regexes:
    print(f"Seeking '{regex.pattern} ->'", end=" ")

    if regex.search(text):
        print('match!')
    else:
        print('no match')

