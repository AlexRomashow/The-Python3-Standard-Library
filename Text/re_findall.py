import re

text = 'abbaaabbbbaaaaa'
pattern = 'ab'

for match in re.findall(pattern, text):
    print(f'Found {match}')
