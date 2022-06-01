import pickle
import sqlite3

db_filename = 'todo.db'

def adapter_func(obj):
    """Преобразует данные, хранящиеся в памяти,
    в представление хранилища.
    """
    print('adapter_func({})\n'.format(obj))
    return pickle.dumps(obj)

def converter_func(data):
    """Преобразует данные, находящиеся в хранилище, в
    представление данных, хранящихся в памяти.
    """
    print('converter_func({!r})\n'.format(data))
    return pickle.loads(data)

class MyObj:
    
    def __init__(self, arg):
        self.arg = arg
    
    def __str__(self):
        return 'MyObj({!r})'.format(self.arg)

# Регистрация функций для манипулирования типами
sqlite3.register_adapter(MyObj, adapter_func)
sqlite3.register_converter ("MyObj", converter_func)

# Создание объектов для сохранения. Используйте список
# кортежей, чтобы последовательность можно бьшо передать
# непосредственно методу executemany().
to_save = [
    (MyObj('this is а value to save'),),
    (MyObj(42),),
]

with sqlite3.connect(
        db_filename,
        detect_types=sqlite3.PARSE_DECLTYPES) as conn:
    # Создание таблицы со столбцами типа "MyObj"
    conn.execute("""
    create table if not exists obj (
    id  integer primary key autoincrement not null,
    data MyObj
    )
    """)
    cursor = conn.cursor()

    # Вставка объектов в базу данных
    cursor.executemany("insert into obj (data) values (?)",
            to_save)

# Запрос объектов, только что сохраненных в базе данных
cursor.execute("select id, data from obj")
for obj_id, obj in cursor.fetchall():
    print('Retrieved', obj_id, obj)
    print('with type', type(obj))
    print()
