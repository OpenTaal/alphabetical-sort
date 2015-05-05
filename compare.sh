cd reference
./preprocess.py
cd ..

# set locale for collating
export LC_COLLATE="nl_NL.UTF-8"


### Pyhton ###

# sort default
./python-sort-default.py reference/sort.txt > result/python-sort-default.txt
diff -Nup reference/sort.txt result/python-sort-default.txt > result/python-sort-default.diff

# sort locale
./python-sort-locale.py reference/sort.txt > result/python-sort-locale.txt
diff -Nup reference/sort.txt result/python-sort-locale.txt > result/python-sort-locale.diff

### coreutils ###

# sort default - according to locale
cat reference/sort.txt|sort > result/coreutils-sort.txt
diff -Nup reference/sort.txt result/coreutils-sort.txt > result/coreutils-sort.diff

# sort dictionary - ignore leading blanks
cat reference/sort.txt|sort -d > result/coreutils-sort-dict.txt
diff -Nup reference/sort.txt result/coreutils-sort-dict.txt > result/coreutils-sort-dict.diff

# sort version - natural sort of (version) numbers within text
cat reference/sort.txt|sort -V > result/coreutils-sort-version.txt
diff -Nup reference/sort.txt result/coreutils-sort-version.txt > result/coreutils-sort-version.diff

# sort ignore case - fold lower case to upper case characters
cat reference/sort.txt|sort -f > result/coreutils-sort-fold.txt
diff -Nup reference/sort.txt result/coreutils-sort-fold.txt > result/coreutils-sort-fold.diff

# sort dictionary and version sort (order of these options is not important)
cat reference/sort.txt|sort -dV > result/coreutils-sort-dict-version.txt
diff -Nup reference/sort.txt result/coreutils-sort-dict-version.txt > result/coreutils-sort-dict-version.diff

# reverse sort
sort -r reference/sort-reverse.txt > result/coreutils-sort-reverse.txt
diff -Nup reference/sort-reverse.txt result/coreutils-sort-reverse.txt > result/coreutils-sort-reverse.diff

# retrograde sort
rev reference/sort-retrograde.txt|sort|rev > result/coreutils-sort-retrograde.txt
diff -Nup reference/sort-retrograde.txt result/coreutils-sort-retrograde.txt > result/coreutils-sort-retrograde.diff

# reverse retrograde sort
rev reference/sort-reverse-retrograde.txt|sort -r|rev > result/coreutils-sort-reverse-retrograde.txt
diff -Nup reference/sort-reverse-retrograde.txt result/coreutils-sort-reverse-retrograde.txt > result/coreutils-sort-reverse-retrograde.diff





# sort custom
cat reference/sort.txt|sed -f substitute.sed|sort|sed -f restore.sed > result/coreutils-sort-custom3.txt
diff -Nup reference/sort.txt result/coreutils-sort-custom3.txt > result/coreutils-sort-custom3.diff

# custom sort
#cat reference/sort.txt|sed -f away.sed|sort|sed -f back.sed > result/coreutils-sort-custom.txt
#diff -Nup reference/sort.txt coreutils-sort-custom.txt > result/coreutils-sort-custom.diff

# custom sort 2
#cat reference/sort.txt|sed -f away2.sed|sort|sed -f back2.sed > result/coreutils-sort-custom2.txt
#diff -Nup reference/sort.txt coreutils-sort-custom2.txt > result/coreutils-sort-custom2.diff

# custom sort 4
#cat reference/sort.txt|sed -f away4.sed|sort|sed -f back4.sed > result/coreutils-sort-custom4.txt
#diff -Nup reference/sort.txt coreutils-sort-custom4.txt > result/coreutils-sort-custom4.diff
