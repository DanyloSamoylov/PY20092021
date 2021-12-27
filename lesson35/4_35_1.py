"""
A shared counter

Make a class called Counter, and make it a subclass of the Thread class in the Threading module.
Make the class have two global variables, one called counter set to 0, and another called rounds set to 100.000.
Now implement the run() method, let it include a simple for-loop that iterates through rounds (e.i. 100.000 times)
and for each time increments the value of the counter by 1. Create 2 instances of the thread and start them,
then join them and check the result of the counter, it should be 200.000, right?
Run it a couple of times and consider some different reasons why you get the answer that you get.
"""

import threading


class Counter(threading.Thread):
    counter = 0
    rounds = 100_000

    def __init__(self, target=None, name=None, args=(), kwargs=None, daemon=False):
        super().__init__(target=target, name=name, args=(), kwargs=kwargs, daemon=daemon)
        self.lock = kwargs.get('lock')

    def run(self):
        for _ in range(self.rounds):
            self.lock.acquire()
            self.__class__.counter += 1
            self.lock.release()


lock = threading.Lock()

thread_1 = Counter(kwargs={'lock': lock})
thread_2 = Counter(kwargs={'lock': lock})

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
print(Counter.counter)




