from http import cookies
import datetime

def show_cookie(c):
    print(c)
    for key, morsel in c.items():
        print()
        print('key =', morsel.key)
        print('value = ', morsel.value)
        print('coded_value = ', morsel.coded_value)
        for name in morsel.keys():
            if morsel[name]:
                print(f'{name} = {morsel[name]}')

c = cookies.SimpleCookie()

# Куки, значение которого должно быть закодировано для
# того, чтобы поместить его в заголовок
c['encoded_value_cookie'] = '"cookie,value;"'
c['encoded_value_cookie']['comment'] = 'Has escaped punctuation'

# Куки, который применим только к части сайта
c['restricted_cookie'] = 'cookie_value'
c['restricted_cookie']['path'] = '/sub/path'
c['restricted_cookie']['domain'] = 'PyMOTW'
c['restricted_cookie']['secure'] = True

# Куки, срок действия которого истекает через 5 минут
c['with_max_age'] = 'expires in 5 minutes'
c['with_max_age']['max-age'] = 300 # seconds

# Куки, срок действия которого истекает к указанному времени
c['expires_at_time'] = 'cookie_value'
time_to_live = datetime.timedelta(hours=1)
expires = (datetime.datetime(2009, 2, 14, 18, 30, 14) +
        time_to_live)

# Формат даты: Wdy, DD-Mon-YY HH:MM:SS GMT
expires_at_time = expires.strftime('%a, %d %b %Y %H:%M:%S')
c['expires_at_time']['expires'] = expires_at_time

show_cookie(c)
