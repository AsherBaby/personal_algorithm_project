from threading import Thread

def print_rain(n):
    for i in range(n):
        print('|'*10)

def print_snow(n):
    for i in range(n):
        print('*'*10)

t1 = Thread(target=print_rain, args=(20,))
t2 = Thread(target=print_snow, args=(20,))
t1.start()
t2.start()
