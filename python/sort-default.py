#!/usr/bin/env python3

from sys import argv


if __name__ == '__main__':
    if len(argv) != 2:
        exit(0)
    words = []
    with open(argv[1]) as input_file:
        for line in input_file:
            word = line[:-1]
            words.append(word)
    words.sort()
    for word in words:
        print('{}'.format(word))
