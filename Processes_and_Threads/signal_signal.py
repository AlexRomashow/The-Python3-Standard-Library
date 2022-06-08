import signal
import os
import time

def receive_signal(signum, stack):
    print('Received:', signum)

# Регистрация дескрипторов сигналов
signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)

# Вывод ID процесса, который впоследствии можно будет
# использовать c командой kill для отправки сигналов этой программе
print('My PID is:', os.getpid())

while True:
    print('Waiting...')
    time.sleep(3)
