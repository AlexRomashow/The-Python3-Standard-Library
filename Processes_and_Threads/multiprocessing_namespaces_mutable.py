import multiprocessing

def producer(ns, event):
    # НЕ ОБНОВЛЯТЬ ГЛОБАЛЬНОЕ ЗНАЧЕНИЕ!
    ns.my_list.append('This is the value')
    event.set()

def consumer(ns, event):
    print('Before event:', ns.my_list)
    event.wait()
    print('After event:', ns.my_list)

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    namespace = mgr.Namespace()
    namespace.my_list = []

    event = multiprocessing.Event()
    p = multiprocessing.Process(
        target=producer,
        args=(namespace, event),
    )

    c = multiprocessing.Process(
        target=consumer,
        args=(namespace, event),
    )

    c.start ()
    р.start()

    с.join()
    p.join()
