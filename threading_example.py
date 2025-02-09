from threading import *
from time import sleep
import threading

lock = threading.Lock()

class Example(Thread):
    def run(self):
        for i in range(5):
            lock.acquire()
            print("Lock Acquired")
            print("Hello from Example 1")
            sleep(1)
            lock.release()

class Example2(Thread):
    def run(self):
        for i in range(5):
            lock.acquire()
            print("Lock Acquired")
            print("Hello from Example 2")
            sleep(1)
            lock.release()


example = Example()
exampleTwo = Example2()
example.start()
sleep(0.1)
exampleTwo.start()
example.join()
exampleTwo.join()
print("Finished")