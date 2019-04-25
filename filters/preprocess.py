#!/usr/bin/env python3


if __name__ == '__main__':
    python_custom_file = open('../python-sort-locale-custom.py', 'w')
    with open('../python-sort-locale.py') as python_file:
        for python_line in python_file:
            if 'import sys' in python_line:
                python_custom_file.write('import re\n')
            elif 'words = []' in python_line:
                python_custom_file.write('    conversion = {\n')
                sed_substitute_file = open('greek-substitute.sed', 'w')
                sed_restore_file = open('greek-restore.sed', 'w')
                with open('greek-substitute.tsv') as input_file:
                    for line in input_file:
                        if line != '\n' and line[0] != '#':
                            (char_src, char_dst) = line[:-1].split('	')
                            sed_substitute_file.write('s/{}/{}/g\n'.format(char_src, char_dst))
                            sed_restore_file.write('s/{}/{}/g\n'.format(char_src, char_dst))
                            python_custom_file.write("        '{}': '{}',\n".format(char_src, char_dst))
                python_custom_file.write('    }\n')
                python_custom_file.write('    substitute = {}\n')
                python_custom_file.write('    restore = {}\n')
                python_custom_file.write('    for char in conversion.keys():\n')
                python_custom_file.write("        substitute[conversion[char]] = re.compile('{}'.format(char))\n")
                python_custom_file.write("        restore[char] = re.compile('{}'.format(conversion[char]))\n")
            elif 'words.append(word)' in python_line:
                python_custom_file.write('            for repl in substitute.keys():\n')
                python_custom_file.write('                word = re.sub(substitute[repl], repl, word)\n')
            elif "print('{}'.format(word))" in python_line:
                python_custom_file.write('        for repl in restore.keys():\n')
                python_custom_file.write('            word = re.sub(restore[repl], repl, word)\n')
            python_custom_file.write(python_line)
