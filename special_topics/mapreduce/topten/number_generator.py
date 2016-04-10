#!/usr/bin/env python3
import random
with open('top_ten.txt', 'w') as fh:
    for i in range(10000):
        n = random.randint(0, 999999)
        fh.write('{0}\n'.format(n))
