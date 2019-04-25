#!/usr/bin/env python3

from locale import LC_ALL, setlocale
from sys import argv

from natsort import ns, natsorted


if __name__ == '__main__':
    if len(argv) != 2:
        exit(0)
    words = []
    with open(argv[1]) as input_file:
        for line in input_file:
            word = line[:-1]
            words.append(word)
    setlocale(LC_ALL, 'nl_NL.UTF-8')
#    words = natsorted(words, alg=ns.G)#252
#    words = natsorted(words, alg=ns.G | ns.LF)#241
#    words = natsorted(words, alg=ns.G | ns.L)#157 !!!
#    words = natsorted(words, alg=ns.G | ns.LF | ns.L)#194
#    words = natsorted(words, alg=ns.LF)#194
#    words = natsorted(words, alg=ns.LF | ns.L)#194
#    NOEXP
    words = natsorted(words, alg=ns.L)  # 161 !!!
    for word in words:
        print('{}'.format(word))
