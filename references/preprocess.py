#!/usr/bin/env python3


if __name__ == '__main__':
    chars = []
    output_file = open('sort-characters.txt', 'w')
    with open('sort-characters.tsv', 'r') as input_file:
        for line in input_file:
            if line != '\n' and line[0] != '#':
                char = line[:-1].split('	')[0]
                chars.append(char)
                output_file.write('{}\n'.format(char))

    words = []
    output_file = open('sort.txt', 'w')
    with open('sort.tsv', 'r') as input_file:
        for line in input_file:
            if line != '\n' and line[0] != '#':
                word = line[:-1].split('	')[0]
                words.append(word)
                output_file.write('{}\n'.format(word))
