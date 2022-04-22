import datetime

f = "%a %b %d %H:%M:%S %Y"
today = datetime.datetime.today()
print('ISO:', today)

s = today.strftime(f)
print('strftime:', s)

d = datetime.datetime.strptime(s, f)
print('strptime:', d.strftime(f))
