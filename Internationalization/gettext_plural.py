from gettext import translation
import sys

t = translation('plural', 'locale', fallback=False)
num = int(sys.argv[1])

msg = t.ngettext('{num} means singular.',
                 '{num} means plural.', num)

# Все еще требуется самостоятельно добавлять значения в сообщение
print(msg.format(num=num))
