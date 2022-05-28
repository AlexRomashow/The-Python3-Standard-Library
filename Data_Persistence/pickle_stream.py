import io
import pickle
import pprint

class SimpleObject:

    def __init__(self, name):
        self.name = name
        self.name_backwards = name[::-1]
        return

data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('preserve'))
data.append(SimpleObject('last'))

# Имитировать файл
out_s = io.BytesIO()

# Записать в поток
for o in data:
    print('WRITING : {} ({})'.format(o.name, o.name_backwards))
    pickle.dump(o, out_s)
    out_s.flush()

# Настроить читаемый поток
in_s = io.BytesIO(out_s.getvalue())

# Прочитать данные
while True:
    try:
        о = pickle.load(in_s)
    except EOFError:
        break
    else:
        print('READ: {} ({})'.format(o.name, o.name_backwards))
