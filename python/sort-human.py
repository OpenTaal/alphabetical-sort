#!/usr/bin/env python3

from natsort import humansorted
from locale import LC_ALL, setlocale
from sys import argv


if __name__ == '__main__':
    if len(argv) != 2:
        exit(0)
    words = []
    with open(argv[1]) as input_file:
        for line in input_file:
            word = line[:-1]
            words.append(word)
    setlocale(LC_ALL, 'nl_NL.UTF-8')
    words = humansorted(words)  # same as natsorted(words, alg=ns.LOCALE)
    for word in words:
        print('{}'.format(word))
