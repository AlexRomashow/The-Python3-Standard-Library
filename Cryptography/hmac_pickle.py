import hashlib
import hmac
import io
import pickle
import pprint

def make_digest(message):
    "Вернуть дайджест сообщения."
    hash = hmac.new(
        b'secret-shared-key-goes-here',
        message,
        hashlib.sha1,
    )
    return hash.hexdigest().encode('utf-8')

class SimpleObject:
    """Продемонстрировать проверку дайджестов перед десериализацией."""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

# Имитация записываемого сокета или потока c помощью буфера
out_s = io.BytesIO()

# Запись корректного объекта в поток
# digest\nlength\npickle
o = SimpleObject('digest matches')
pickled_data = pickle.dumps(o)
digest = make_digest(pickled_data)
header = b'%s %d\n' % (digest, len(pickled_data))
print('WRITING: {}'.format(header) )
out_s.write (header)
out_s.write(pickled_data)

# Запись некорректного объекта в поток
o = SimpleObject('digest does not match')
pickled_data = pickle.dumps(o)
digest = make_digest(b'not the pickled data at all')
header = b'%s %d\n' % (digest, len(pickled_data))
print('\nWRITING: {}'.format(header))
out_s.write(header)
out_s.write(pickled_data)

out_s.flush()

# Имитация читаемого сокета или канала
in_s = io.BytesIO(out_s.getvalue())

# Чтение данных
while True:
    first_line = in_s.readline()
    if not first_line:
        break
    incoming_digest, incoming_length = first_line.split(b' ')
    incoming_length = int(incoming_length.decode('utf-8'))
    print('\nREAD:', incoming_digest, incoming_length)
    
    incoming_pickled_data = in_s.read(incoming_length)

    actual_digest = make_digest(incoming_pickled_data)
    print('ACTUAL:', actual_digest)
    
    if hmac.compare_digest(actual_digest, incoming_digest):
        obj = pickle.loads(incoming_pickled_data)
        print('OK:', obj)
    else:
        print('WARNING: Data corruption')
