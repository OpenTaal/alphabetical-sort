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

# dictionary and version sort
# (order of these options is not important)
cat reference-sorted.txt|sort -dV > coreutils-sort-dict-version.txt
diff -Nup reference-sorted.txt coreutils-sort-dict-version.txt > coreutils-sort-dict-version.diff
