import mmap
import shutil

# Копирование файла примера
shutil.copyfile('lorem.txt', 'lorem_copy.txt')

word = b'consectetuer'
reverse = word[::-1]
print('Looking for:', word)
print('Replacing with:', reverse)

with open('lorem_copy.txt', 'r+') as f:
    with mmap.mmap(f.fileno(), 0) as m:
        print('Before:\n{}'.format(m.readline().rstrip()))
        m.seek(0) # перейти в начало

        loc = m.find(word)
        m[loc:loc + len(word)] = reverse
        m.flush()

        m.seek(0) # перейти в начало
        print('After :\n{}'.format(m.readline().rstrip()))

        f.seek(0) # перейти в начало
        print('File :\n{}'.format(f.readline().rstrip()))
