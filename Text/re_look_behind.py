import re

twitter = re.compile(
    '''
    # Идентификатор пользователя в Твиттере: @username
    (?<=@)
    ([\w\d_]+) # Имя пользователя
    ''',
    re.VERBOSE)

text = '''This text includes two Twitter handles.
One for @ThePSF, and one for the author, @doughellmann.
'''

print(text)
for match in twitter.findall(text):
    print('Handle:', match)
