#!/usr/bin/env python3

import locale
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit(0)
    words = []
    with open(sys.argv[1], 'r') as input_file:
        for line in input_file:
            word = line[:-1]
            words.append(word)
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    words = sorted(words, key=locale.strxfrm)
    for word in words:
        print('{}'.format(word))
