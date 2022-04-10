import re

pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print(f"Found '{match.re.pattern}' \nin '{match.string}'\nfrom {s} to {e} ('{text[s:e]}')")
