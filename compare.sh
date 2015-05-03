./preprocess.py
diff -Nup reference-sorted.txt python-sorted.txt > python-sorted.diff

# default sort
cat reference-sorted.txt|sort > coreutils-sort.txt
diff -Nup reference-sorted.txt coreutils-sort.txt > coreutils-sort.diff

# dictionary sort
# ignore leading blanks
cat reference-sorted.txt|sort -d > coreutils-sort-dict.txt
diff -Nup reference-sorted.txt coreutils-sort-dict.txt > coreutils-sort-dict.diff

# version sort
# natural sort of (version) numbers within text
cat reference-sorted.txt|sort -V > coreutils-sort-version.txt
diff -Nup reference-sorted.txt coreutils-sort-version.txt > coreutils-sort-version.diff

# ignore case sort
# fold lower case to upper case characters
cat reference-sorted.txt|sort -f > coreutils-sort-fold.txt
diff -Nup reference-sorted.txt coreutils-sort-fold.txt > coreutils-sort-fold.diff

# dictionary and version sort
# (order of these options is not important)
cat reference-sorted.txt|sort -dV > coreutils-sort-dict-version.txt
diff -Nup reference-sorted.txt coreutils-sort-dict-version.txt > coreutils-sort-dict-version.diff

# custom sort
cat reference-sorted.txt|sed -f away.sed|sort|sed -f back.sed > coreutils-sort-custom.txt
diff -Nup reference-sorted.txt coreutils-sort-custom.txt > coreutils-sort-custom.diff

# custom sort 2
cat reference-sorted.txt|sed -f away2.sed|sort|sed -f back2.sed > coreutils-sort-custom2.txt
diff -Nup reference-sorted.txt coreutils-sort-custom2.txt > coreutils-sort-custom2.diff

# retrograde sort
rev reference-sorted-retrograde.txt|sort|rev > coreutils-sort-retrograde.txt
diff -Nup reference-sorted-retrograde.txt coreutils-sort-retrograde.txt > coreutils-sort-retrograde.diff
