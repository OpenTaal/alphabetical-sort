#!/usr/bin/env python3

import locale
import re
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
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
        substitute[conversion[char]] = re.compile('{}'.format(char))
        restore[char] = re.compile('{}'.format(conversion[char]))
    words = []
    with open(sys.argv[1], 'r') as input_file:
        for line in input_file:
            word = line[:-1]
            for repl in substitute.keys():
                word = re.sub(substitute[repl], repl, word)
            words.append(word)
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    words = sorted(words, key=locale.strxfrm)
    for word in words:
        for repl in restore.keys():
            word = re.sub(restore[repl], repl, word)
        print('{}'.format(word))
