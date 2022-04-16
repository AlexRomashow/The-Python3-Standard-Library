from queue import Queue
import threading
import time
import urllib
from urllib.parse import urlparse

import feedparser

# Установка некоторых глобальных переменных
num_fetch_threads = 2
enclosure_queue = Queue()

# В реальном приложении вы не будете задавать данные в коде...
feed_urls = ['http://talkpython.fm/episodes/rss',]

def message(s):
    print('{}: {}'.format(threading.current_thread().name, s))

def download_enclosure(q):
    '''Это функция рабочего потока.
    Она обрабатывает элементы очереди один за другим.
    Потоки этого процесса-демона входят в бесконечный
    цикл и завершаются, только когда завершается
    основной поток.
    '''
    while True:
        message('looking for the next enclosure')
        url = q.get()
        filename = url.rpartition('/')[-1]
        message('downloading {}'.format(filename))
        response = urllib.request.urlopen(url)
        data = response.read()
        # Сохранить загруженный файл в текущем каталоге
        message('writting to {}'.format(filename))
        with open(filename, 'wb') as outfile:
            outfile.write(data)
        q.task_done()

# Настройка потоков для извлечения вложений
for i in range(num_fetch_threads):
    worker = threading.Thread(
        target=download_enclosures,
        args=(enclosure_queue,),
        name='worker-{}'.format(i),
        )
    worker.setDaemon(True)
    worker.start()

# Загрузка каналов и помещение URL-адресов вложений в очередь
for url in feed_urls:
    response = feedparser.parse(url, agent='fetch_podcasts.py')
    for entry in response['entries'][:5]:
        for enclosure in entry.get('enclosures', []):
            parsed_url = urlparse(enclosure['url'])
            message('quering {}'.format(
                parsed_url.path.rpartition('/')[-1]))
            enclosure_queue.put(enclosure['url'])

# Дождаться исчерпания очереди, что будет свидетельствовать
# о завершении обработки всех закачек
message('*** main thread waiting')
enclosure_queue.join()
message('*** done')







