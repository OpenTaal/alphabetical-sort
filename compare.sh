cd references
./preprocess.py
cd ..

# set locale for collating
export LC_COLLATE="nl_NL.UTF-8"


### Pyhton ###

# sort default
./python-sort-default.py references/sort.txt > results/python-sort-default.txt
diff -Nup references/sort.txt results/python-sort-default.txt > differences/python-sort-default.diff

# sort locale
./python-sort-locale.py references/sort.txt > results/python-sort-locale.txt
diff -Nup references/sort.txt results/python-sort-locale.txt > differences/python-sort-locale.diff

# sort locale custom
./python-sort-locale-custom.py references/sort.txt > results/python-sort-locale-custom.txt
diff -Nup references/sort.txt results/python-sort-locale-custom.txt > differences/python-sort-locale-custom.diff


### coreutils ###

# sort default - according to locale
cat references/sort.txt|sort > results/coreutils-sort.txt
diff -Nup references/sort.txt results/coreutils-sort.txt > differences/coreutils-sort.diff

# sort custom
cat references/sort.txt|sed -f filters/greek-substitute.sed|sort|sed -f filters/greek-restore.sed > results/coreutils-sort-custom.txt
diff -Nup references/sort.txt results/coreutils-sort-custom.txt > differences/coreutils-sort-custom.diff

# sort dictionary - ignore leading blanks
cat references/sort.txt|sort -d > results/coreutils-sort-dict.txt
diff -Nup references/sort.txt results/coreutils-sort-dict.txt > differences/coreutils-sort-dict.diff

# sort version - natural sort of (version) numbers within text
cat references/sort.txt|sort -V > results/coreutils-sort-version.txt
diff -Nup references/sort.txt results/coreutils-sort-version.txt > differences/coreutils-sort-version.diff

# sort ignore case - fold lower case to upper case characters
cat references/sort.txt|sort -f > results/coreutils-sort-fold.txt
diff -Nup references/sort.txt results/coreutils-sort-fold.txt > differences/coreutils-sort-fold.diff

# sort dictionary and version sort (order of these options is not important)
cat references/sort.txt|sort -dV > results/coreutils-sort-dict-version.txt
diff -Nup references/sort.txt results/coreutils-sort-dict-version.txt > differences/coreutils-sort-dict-version.diff

# reverse sort
sort -r references/sort-reverse.txt > results/coreutils-sort-reverse.txt
diff -Nup references/sort-reverse.txt results/coreutils-sort-reverse.txt > differences/coreutils-sort-reverse.diff

# retrograde sort
rev references/sort-retrograde.txt|sort|rev > results/coreutils-sort-retrograde.txt
diff -Nup references/sort-retrograde.txt results/coreutils-sort-retrograde.txt > differences/coreutils-sort-retrograde.diff

# reverse retrograde sort
rev references/sort-reverse-retrograde.txt|sort -r|rev > results/coreutils-sort-reverse-retrograde.txt
diff -Nup references/sort-reverse-retrograde.txt results/coreutils-sort-reverse-retrograde.txt > differences/coreutils-sort-reverse-retrograde.diff
