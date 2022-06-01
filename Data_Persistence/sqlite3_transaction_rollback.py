import sqlite3

db_filename = 'todo.db'

def show_projects(conn):
    cursor = conn.cursor()
    cursor.execute('select name, description from project')
    for name, desc in cursor.fetchall():
        print(' ', name)

with sqlite3.connect(db_filename) as conn:
    print('Before changes:')
    show_projects(conn)
    try:
        # Вставить строку
        cursor = conn.cursor()
        cursor.execute("""delete from project
                    where name = 'virtualenvwrapper'
        """)
        # Отобразить результаты
        print('\nAfter delete:')
        show_projects(conn)

        # Искусственно возбудить исключение
        raise RuntimeError('simulated error')
    
    except Exception as err:
        # Отказаться от изменений
        print('ERROR:', err)
        conn.rollback()
    
    else:
        # Сохранить изменения
        conn.commit()
    
    # Отобразить результаты
    print('\nAfter rollback:')
    show_projects(conn)
