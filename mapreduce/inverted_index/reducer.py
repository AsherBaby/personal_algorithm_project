#!/usr/bin/env python
import sys

def main():
    last = sys.stdin.readline().strip()
    if not last:
        return
    [last_word, dID] = last.split()
    d_list = set(dID)
    for line in sys.stdin:
        [word, dID] = line.strip().split()
        if word == last_word:
            d_list.add(dID)
        else:
            print('{}\t{}'.format(last_word, '\t'.join(d_list)))
            last_word = word
            d_list = set(dID)
    print('{}\t{}'.format(last_word, '\t'.join(d_list)))

main()
