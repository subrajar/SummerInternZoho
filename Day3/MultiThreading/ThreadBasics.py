import threading
import time


def hello():
    time.sleep(1)
    print 'Hello World'


t1 = threading.Thread(target=hello)
t2 = threading.Thread(target=hello)
t1.start()
t2.start()
t2.join()
t1.join()
print 'done'
