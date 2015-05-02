#!/usr/bin/env python3

"""
Name		preprocess.py
Description	Converts annotated sort-order.tsv to one-column sort-order.txt
Author		Sander van Geloven <sander.vangeloven@opentaal.org>
License		MIT
"""


if __name__ == '__main__':
    chars = []
    sort_order_file = open('sort-order.txt', 'w')
    with open('sort-order.tsv', 'r') as sort_order_annotated_file:
        for line in sort_order_annotated_file:
            if line != '\n' and line[0] != '#':
                char = line[:-1].split('	')[0]
                chars.append(char)
                sort_order_file.write('{}\n'.format(char))
#    python_sort_order_file = open('python-sort-order.txt', 'w')
#    for char in sorted(chars):
#        python_sort_order_file.write('{}\n'.format(char))

    words = []
    reference_sorted_file = open('reference-sorted.txt', 'w')
    with open('reference-sorted.tsv', 'r') as reference_sorted_annotated_file:
        for line in reference_sorted_annotated_file:
            if line != '\n' and line[0] != '#':
                word = line[:-1].split('	')[0]
                words.append(word)
                reference_sorted_file.write('{}\n'.format(word))
    python_reference_sorted_file = open('python-sorted.txt', 'w')
    for word in sorted(words):
        python_reference_sorted_file.write('{}\n'.format(word))
