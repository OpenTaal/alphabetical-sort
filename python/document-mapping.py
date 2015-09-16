#!/usr/bin/env python3

from locale import LC_ALL, setlocale, strxfrm
from unicodedata import name


if __name__ == '__main__':
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

    reverse = {}
    for key in conversion.keys():
        reverse[conversion[key]] = key
    for key in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z', ):
        reverse[key] = key
        key = key.upper()
        reverse[key] = key

    setlocale(LC_ALL, 'nl_NL.UTF-8')
    for key in sorted(reverse.keys(), key=strxfrm):
        print('{}\t{}\t{}'.format(key, reverse[key], name(reverse[key])))
