#!/usr/bin/env python3

"""
Name		preprocess.py
Description	Converts annotated sort-order.tsv to one-column sort-order.txt
Author		Sander van Geloven <sander.vangeloven@opentaal.org>
License		MIT
"""


if __name__ == '__main__':
    sort_order_file = open('sort-order.txt', 'w')
    with open('sort-order.tsv', 'r') as sort_order_annotated_file:
        for line in sort_order_annotated_file:
            sort_order_file.write('{}\n'.format(line.split('	')[0]))
