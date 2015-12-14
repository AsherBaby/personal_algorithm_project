#!/usr/bin/env python
import sys

def main():
    last_word = sys.stdin.readline().rstrip().split()
    if not i:
        return
    last_word= last_word[0]
    count = 1
    for line in sys.stdin:
        word = line.rstrip().split()[0]
        if word == last_word:
            count += 1
        else:
            print('{}\t{}'.format(i, count))
            last_word= j
            count = 1
    print('{}\t{}'.format(last_word, count))

main()
