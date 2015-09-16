#!/usr/bin/env python3

from locale import LC_ALL, setlocale
from re import compile, sub
from sys import argv

from natsort import ns, natsorted


if __name__ == '__main__':
    if len(argv) != 2:
        exit(0)
    conversion = {
        'α': 'ḁ',
        'β': 'ḇ',
        'χ': 'ƈ',
        'δ': 'ɖ',
        'Δ': 'Ḏ',
        'ε': 'ḙ',
        'η': 'ḛ',
        'φ': 'ḟ',
        'Φ': 'Ḟ',
        'γ': 'ɠ',
        'Γ': 'Ɠ',
        'ι': 'ḭ',
        'κ': 'ƙ',
        'λ': 'ḻ',
        'Λ': 'Ḻ',
        'µ': 'ṃ',
        'ν': 'ŋ',
        'ω': 'ọ',
        'Ω': 'Ọ',
        'π': 'ṕ',
        'Π': 'Ṕ',
        'ψ': 'ṗ',
        'Ψ': 'Ṗ',
        'ρ': 'ṟ',
        'σ': 'ṣ',
        'ς': 'ṩ',
        'Σ': 'Ṣ',
        'τ': 'ṱ',
        'θ': 'ṯ',
        'Θ': 'Ṯ',
        'υ': 'ṵ',
        'ξ': 'ȥ',
        'Ξ': 'Ȥ',
        'ζ': 'ȥ',
    }
    substitute = {}
    restore = {}
    for char in conversion.keys():
        substitute[conversion[char]] = compile('{}'.format(char))
        restore[char] = compile('{}'.format(conversion[char]))
    words = []
    with open(argv[1], 'r') as input_file:
        for line in input_file:
            word = line[:-1]
            for repl in substitute.keys():
                word = sub(substitute[repl], repl, word)
            words.append(word)
    setlocale(LC_ALL, 'nl_NL.UTF-8')
# See https://github.com/SethMMorton/natsort/blob/master/natsort/ns_enum.py
#    words = natsorted(words, alg=ns.L | ns.N | ns.V)
    words = natsorted(words, alg=ns.L)
    for word in words:
        for repl in restore.keys():
            word = sub(restore[repl], repl, word)
        print('{}'.format(word))
