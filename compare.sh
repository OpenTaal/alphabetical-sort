./preprocess.py

# set locale for collating
export LC_COLLATE="nl_NL.UTF-8"


### Pyhton ###

# sort default
./python-sort-default.py reference/sort.txt > python-sort-default.txt
diff -Nup reference/sort.txt python-sort-default.txt > python-sort-default.diff

# sort locale
./python-sort-locale.py reference/sort.txt > python-sort-locale.txt
diff -Nup reference/sort.txt python-sort-locale.txt > python-sort-locale.diff

### coreutils ###

# sort default - according to locale
cat reference/sort.txt|sort > coreutils-sort.txt
diff -Nup reference/sort.txt coreutils-sort.txt > coreutils-sort.diff

# sort dictionary - ignore leading blanks
cat reference/sort.txt|sort -d > coreutils-sort-dict.txt
diff -Nup reference/sort.txt coreutils-sort-dict.txt > coreutils-sort-dict.diff

# sort version - natural sort of (version) numbers within text
cat reference/sort.txt|sort -V > coreutils-sort-version.txt
diff -Nup reference/sort.txt coreutils-sort-version.txt > coreutils-sort-version.diff

# sort ignore case - fold lower case to upper case characters
cat reference/sort.txt|sort -f > coreutils-sort-fold.txt
diff -Nup reference/sort.txt coreutils-sort-fold.txt > coreutils-sort-fold.diff

# sort dictionary and version sort (order of these options is not important)
cat reference/sort.txt|sort -dV > coreutils-sort-dict-version.txt
diff -Nup reference/sort.txt coreutils-sort-dict-version.txt > coreutils-sort-dict-version.diff

# reverse sort
sort -r reference/sort-reverse.txt > coreutils-sort-reverse.txt
diff -Nup reference/sort-reverse.txt coreutils-sort-reverse.txt > coreutils-sort-reverse.diff

# retrograde sort
rev reference/sort-retrograde.txt|sort|rev > coreutils-sort-retrograde.txt
diff -Nup reference/sort-retrograde.txt coreutils-sort-retrograde.txt > coreutils-sort-retrograde.diff

# reverse retrograde sort
rev reference/sort-reverse-retrograde.txt|sort -r|rev > coreutils-sort-reverse-retrograde.txt
diff -Nup reference/sort-reverse-retrograde.txt coreutils-sort-reverse-retrograde.txt > coreutils-sort-reverse-retrograde.diff





# custom sort
#catreference/sort.txt|sed -f away.sed|sort|sed -f back.sed > coreutils-sort-custom.txt
#diff -Nupreference/sort.txt coreutils-sort-custom.txt > coreutils-sort-custom.diff

# custom sort 2
#catreference/sort.txt|sed -f away2.sed|sort|sed -f back2.sed > coreutils-sort-custom2.txt
#diff -Nupreference/sort.txt coreutils-sort-custom2.txt > coreutils-sort-custom2.diff

# custom sort 3
catreference/sort.txt|sed -f away3.sed|sort|sed -f back3.sed > coreutils-sort-custom3.txt
diff -Nupreference/sort.txt coreutils-sort-custom3.txt > coreutils-sort-custom3.diff

# custom sort 4
#catreference/sort.txt|sed -f away4.sed|sort|sed -f back4.sed > coreutils-sort-custom4.txt
#diff -Nupreference/sort.txt coreutils-sort-custom4.txt > coreutils-sort-custom4.diff
