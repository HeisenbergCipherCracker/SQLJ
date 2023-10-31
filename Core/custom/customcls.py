from threading import Thread
from colorama import Fore, init

init()

class SimpleThread(Thread):
    def __init__(self, target, name):
        super().__init__(target=target, name=name)

    def run(self):
        self._target()

# Create an instance of ThreadCustom
def foo():
    print(Fore.RED + "hello")

def foo2():
    print("45")

t1 = ThreadCustom(target=foo, name="Thread 1")
t2 = ThreadCustom(target=foo2, name="Thread 2")
t1.start()
t2.start()
t1.join()
t2.join()