import gettext

t = gettext.translation(
    'example_domain', 'locale',
    fallback=True,
)

_ = t.gettext

print(_('This message is in the script.'))
