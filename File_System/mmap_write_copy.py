import mmap
import shutil

# Копирование файла примера
shutil.copyfile('lorem.txt', 'lorem_copy.txt')

word = b'consectetuer'
reverse = word[::-1]

with open('lorem_copy.txt', 'r+') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY) as m:
        print('Memory Before:\n{}'.format(m.readline().rstrip()))
        print('File Before:\n{}\n'.format(f.readline().rstrip()))

        m.seek(0) # перейти в начало
        loc = m.find(word)

        m.seek(0) # перейти в начало
        print('Memory After:\n{}'.format(m.readline().rstrip()))

        f.seek(0)
        print('File After:\n{}'.format(f.readline().rstrip()))
