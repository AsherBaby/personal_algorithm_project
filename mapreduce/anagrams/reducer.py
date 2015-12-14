#!/usr/bin/env python

import sys

def main():
    i = sys.stdin.readline().rstrip().split()
    if not i:
        return
    last_anagram = i[0]
    group = [i[1]]
    for line in sys.stdin:
        [anagram, word] = line.rstrip().split()
        if anagram == last_anagram:
            group.append(word)
        else:
            print('\t'.join(group))
            last_anagram = anagram
            group = [word]
    print('\t'.join(group))

main()
