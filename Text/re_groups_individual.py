import re

text = 'This is some text -- with punctuation.'
print('Input text:', text)

# Слово, начинающееся c 't', за которым следует другое слово
regex = re.compile(r'(\bt\w+)\W+(\w+)')
print('Pattern:', regex.pattern)

match = regex.search(text)
print('Entire match:', match.group(0))
print('Word starting with "t":', match.group(1))
print('Word after "t" word:', match.group(2))
