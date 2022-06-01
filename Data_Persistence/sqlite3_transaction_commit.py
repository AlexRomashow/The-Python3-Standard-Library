import sqlite3

db_filename = 'todo.db'

def show_projects(conn):
    cursor = conn.cursor()
    cursor.execute('select name, description from project')
    for name, desc in cursor.fetchall():
        print(' ', name)

with sqlite3.connect(db_filename) as conn1:
    print('Before changes:')
    show_projects(conn1)

# Вставка в один курсор
cursor1 = conn1.cursor()
cursor1.execute("""
insert into project (name, description, deadline)
values ('virtualenvwrapper', 'Virtualenv Extensions',
        '2011-01-01')
""")

print('\nAfter changes in connl:')
show_projects(conn1)

# Выборка из другого соединения до фиксации
# изменений, выполненных в первом соединении
print('\nBefore commit:')
with sqlite3.connect(db_filename) as conn2:
    show_projects(conn2)

# Фиксация изменений c последующей
# выборкой из другого соединения
conn1.commit()
print('\nAfter commit:')
with sqlite3.connect(db_filename) as conn3:
    show_projects(conn3)
