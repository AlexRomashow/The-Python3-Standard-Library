import sched
import threading
import time

scheduler = sched.scheduler(time.time, time.sleep)

# Задать глобальную переменную, значение которой будет
# изменяться потоками
counter = 0

def increment_counter(name):
    global counter
    print('EVENT:', time.ctime(time.time()), name)
    counter += 1
    print('NOW:', counter)

print('START:', time.ctime(time.time()))
e1 = scheduler.enter(2, 1, increment_counter, ('E1',))
e2 = scheduler.enter(3, 1, increment_counter, ('E2',))

# Запустить поток для выполнения событий
t = threading.Thread(target=scheduler.run)
t.start()

# Отменить в основном потоке первое из запланированных событий
scheduler.cancel(e1)

# Выждать, пока не завершится выполнение планировщика в потоке
t.join()
print('FINAL:', counter)
