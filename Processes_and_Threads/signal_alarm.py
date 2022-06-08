import signal
import time

def receive_alarm(signum, stack):
    print('Alarm:', time.ctime())

# Вызвать receive_alarm через 2 секунды
signal.signal(signal.SIGALRM, receive_alarm)
signal.alarm(2)

print('Before:', time.ctime())
time.sleep(4)
print('After:', time.ctime())
