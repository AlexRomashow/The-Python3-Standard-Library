import calendar
import sys

year = int(sys.argv[1])

# Отобразить каждый месяц
for month in range(1, 13):

    # Вычислить даты для каждой недели, перекрывающейся
    # c данным месяцем
    c = calendar.monthcalendar(year, month)
    first_week = c[0]
    second_week = c[1]
    third_week = c[2]

    # Если первая неделя содержит четверг,
    # то второй четверг приходится на вторую неделю.
    # В противном случае второй четверг должен
    # приходиться на третью неделю.

    if first_week[calendar.THURSDAY]:
        meeting_date = second_week[calendar.THURSDAY]
    else:
        meeting_date = third_week[calendar.THURSDAY]

    print('{:>3}: {:>2}'.format(calendar.month_abbr[month], meeting_date))
