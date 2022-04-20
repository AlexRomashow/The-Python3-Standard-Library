import hashlib
import time

# Данные, используемые для расчета контрольных сумм md5
data = open(__file__, 'rb').read()

for i in range(5):
    h = hashlib.sha1()
    print(time.ctime(), ': {:0.3f}'.format(
        time.time(),))
    for i in range(300000):
        h.update(data)
    cksum = h.digest()
