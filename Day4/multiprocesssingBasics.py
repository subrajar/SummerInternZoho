import multiprocessing
import time


def hi():
    time.sleep(1)
    print 'Hello World'


processes = []
for i in range(10):
    p = multiprocessing.Process(target=hi)
    p.start()
    processes.append(p)
for p1 in processes:
    p1.join()
print 'done'
