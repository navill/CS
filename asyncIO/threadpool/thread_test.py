import threading
import os
from queue import Queue
import time

def func1():
    for i in range(1, 11):
        print(i, end="  ")
    print()

def func2():
    for i in range(20, 31):
        print(i, end="  ")
    print()

def func3():
    for i in range(100, 111):
        print(i, end="  ")
    print()

class Worker(threading.Thread):
    def __init__(self, pool, id):
        super().__init__()
        self.pool=pool
        self.tid=id

    def __del__(self):
        print('thread [{}] is stopped'.format(self.tid))

    def run(self):
        while True:
            print('starting process [{}]'.format(self.tid))
            self.pool.cv.acquire()
            while not self.pool.stopped and self.pool.tasks.empty():
                print('waiting  [{}]'.format(self.tid))
                self.pool.cv.wait(timeout=5)

            if self.pool.stopped:
                self.pool.cv.notify()
                print('stopped [{}]'.format(self.tid))
                self.pool.cv.release()
                time.sleep(0.02)
                return

            task=self.pool.tasks.get()
            self.pool.cv.release()
            time.sleep(0.01)

            print('{} running [{}]'.format(task.__name__, self.tid))
            task()

class ThreadPool:
    cv=threading.Condition()
    stopped=False
    def __init__(self):
        self.threads=[Worker(self, i) for i in range(os.cpu_count())]
        self.tasks=Queue()    

        for th in self.threads:
            th.start()

    def add_task(self, fn):
        self.cv.acquire()
        self.tasks.put(fn)
        self.cv.notify()
        self.cv.release()
        time.sleep(0.02)

    def close_all_threads(self):
        self.cv.acquire()
        self.stopped=True
        self.cv.notify()
        self.cv.release()
        time.sleep(0.02)

        for th in self.threads:
            th.join()

if __name__=="__main__":
    tp=ThreadPool()
    for i in range(10):
        tp.add_task(func1)
        tp.add_task(func2)
        tp.add_task(func3)

    print(threading.active_count())
    tp.close_all_threads()
    print(threading.active_count())
    
    


    