from time import sleep
from threading import Lock, Thread

class ThreadSafeATM:

    def __init__(self, init_value):
        self.balance = init_value
        self.lock = Lock()

    def withdraw(self, value):
        print('start to withdraw', flush=True)
        with self.lock:
            print('withdrawing')
            if self.balance >= value:
                self.balance -= value
                for i in range(5, 0, -1):
                    print('withdrawing {}s left...'.format(i))
                    sleep(1)
        print('finish withdrawing', flush=True)

    def deposite(self, value):
        print('start to deposite', flush=True)
        with self.lock:
            print('depositing...')
            self.balance += value
            for i in range(3, 0, -1):
                print('depositing {}s left...'.format(i))
                sleep(1)
        print('finish depositing', flush=True)

atm = ThreadSafeATM(100)  # shared object
t1 = Thread(target=atm.withdraw, args=(50,))
t2 = Thread(target=atm.deposite, args=(100,))
t1.start()
t2.start()
