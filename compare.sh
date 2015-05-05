./preprocess.py

# set locale for collating
export LC_COLLATE="nl_NL.UTF-8"


### Pyhton ###

# sort default
./python-sort-default.py reference-sorted.txt > python-sort-default.txt
diff -Nup reference-sorted.txt python-sort-default.txt > python-sort-default.diff

# sort locale
./python-sort-locale.py reference-sorted.txt > python-sort-locale.txt
diff -Nup reference-sorted.txt python-sort-locale.txt > python-sort-locale.diff

### coreutils ###

# sort default - according to locale
cat reference-sorted.txt|sort > coreutils-sort.txt
diff -Nup reference-sorted.txt coreutils-sort.txt > coreutils-sort.diff

# sort dictionary - ignore leading blanks
cat reference-sorted.txt|sort -d > coreutils-sort-dict.txt
diff -Nup reference-sorted.txt coreutils-sort-dict.txt > coreutils-sort-dict.diff

# sort version - natural sort of (version) numbers within text
cat reference-sorted.txt|sort -V > coreutils-sort-version.txt
diff -Nup reference-sorted.txt coreutils-sort-version.txt > coreutils-sort-version.diff

# sort ignore case - fold lower case to upper case characters
cat reference-sorted.txt|sort -f > coreutils-sort-fold.txt
diff -Nup reference-sorted.txt coreutils-sort-fold.txt > coreutils-sort-fold.diff

# sort dictionary and version sort (order of these options is not important)
cat reference-sorted.txt|sort -dV > coreutils-sort-dict-version.txt
diff -Nup reference-sorted.txt coreutils-sort-dict-version.txt > coreutils-sort-dict-version.diff

# reverse sort
sort -r reference-sorted-reverse.txt > coreutils-sort-reverse.txt
diff -Nup reference-sorted-reverse.txt coreutils-sort-reverse.txt > coreutils-sort-reverse.diff

# retrograde sort
rev reference-sorted-retrograde.txt|sort|rev > coreutils-sort-retrograde.txt
diff -Nup reference-sorted-retrograde.txt coreutils-sort-retrograde.txt > coreutils-sort-retrograde.diff

# reverse retrograde sort
rev reference-sorted-reverse-retrograde.txt|sort -r|rev > coreutils-sort-reverse-retrograde.txt
diff -Nup reference-sorted-reverse-retrograde.txt coreutils-sort-reverse-retrograde.txt > coreutils-sort-reverse-retrograde.diff





# custom sort
#cat reference-sorted.txt|sed -f away.sed|sort|sed -f back.sed > coreutils-sort-custom.txt
#diff -Nup reference-sorted.txt coreutils-sort-custom.txt > coreutils-sort-custom.diff

# custom sort 2
#cat reference-sorted.txt|sed -f away2.sed|sort|sed -f back2.sed > coreutils-sort-custom2.txt
#diff -Nup reference-sorted.txt coreutils-sort-custom2.txt > coreutils-sort-custom2.diff

# custom sort 3
cat reference-sorted.txt|sed -f away3.sed|sort|sed -f back3.sed > coreutils-sort-custom3.txt
diff -Nup reference-sorted.txt coreutils-sort-custom3.txt > coreutils-sort-custom3.diff

# custom sort 4
#cat reference-sorted.txt|sed -f away4.sed|sort|sed -f back4.sed > coreutils-sort-custom4.txt
#diff -Nup reference-sorted.txt coreutils-sort-custom4.txt > coreutils-sort-custom4.diff
