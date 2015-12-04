import random
with open('top_ten.txt', 'w') as fh:
    for i in range(100000):
        n = random.randint(0, 99999999)
        fh.write('{0}\n'.format(n))
