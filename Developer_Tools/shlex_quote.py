import shlex

examples = [
    "Embedded'SingleQuote",
    'Embedded"DoubleQuote',
    'Embedded Space',
    '~SpecialCharacter',
    r'BackXslash',
]
for s in examples:
    print('ORIGINAL  : {}'.format(s))
    print('QUOTED    : {}'.format(shlex.quote(s)))
    print()
