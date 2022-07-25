import multiprocessing

def worker(num):
    """Функция рабочего процессa"""
    print('Worker:', num)

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()
