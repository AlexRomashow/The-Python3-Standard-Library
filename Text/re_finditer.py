import re

text = 'abbaaabbbbaaaaa'
pattern = 'ab'

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()

    print(f'Found {text[s:e]} at {s}:{e}')
