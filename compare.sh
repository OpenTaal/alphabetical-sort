cd references
./preprocess.py
cd ..

# set locale for collating
export LC_COLLATE="nl_NL.UTF-8"
export LC_NUMERIC="nl_NL.UTF-8"


### Pyhton ###

# sort default
./python/sort-default.py references/sort.txt > results/python-sort-default.txt
diff -Nup references/sort.txt results/python-sort-default.txt > differences/python-sort-default.diff

# sort locale
./python/sort-locale.py references/sort.txt > results/python-sort-locale.txt
diff -Nup references/sort.txt results/python-sort-locale.txt > differences/python-sort-locale.diff

# sort locale custom
./python/sort-locale-custom.py references/sort.txt > results/python-sort-locale-custom.txt
diff -Nup references/sort.txt results/python-sort-locale-custom.txt > differences/python-sort-locale-custom.diff

# sort nat
./python/sort-nat.py references/sort.txt > results/python-sort-nat.txt
diff -Nup references/sort.txt results/python-sort-nat.txt > differences/python-sort-nat.diff

# sort nat custom
./python/sort-nat-custom.py references/sort.txt > results/python-sort-nat-custom.txt
diff -Nup references/sort.txt results/python-sort-nat-custom.txt > differences/python-sort-nat-custom.diff

# sort human
./python/sort-human.py references/sort.txt > results/python-sort-human.txt
diff -Nup references/sort.txt results/python-sort-human.txt > differences/python-sort-human.diff

# sort human custom
./python/sort-human-custom.py references/sort.txt > results/python-sort-human-custom.txt
diff -Nup references/sort.txt results/python-sort-human-custom.txt > differences/python-sort-human-custom.diff

# sort real
./python/sort-real.py references/sort.txt > results/python-sort-real.txt
diff -Nup references/sort.txt results/python-sort-real.txt > differences/python-sort-real.diff

# sort real custom
./python/sort-real-custom.py references/sort.txt > results/python-sort-real-custom.txt
diff -Nup references/sort.txt results/python-sort-real-custom.txt > differences/python-sort-real-custom.diff

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
