./preprocess.py
# default sort
cat reference-sorted.txt|sort > coreutils-sort.txt
# dictionary sort
# ignore leading blanks
cat reference-sorted.txt|sort -d > coreutils-sort-dict.txt
# version sort
# natural sort of (version) numbers within text
cat reference-sorted.txt|sort -V > coreutils-sort-version.txt
# dictionary and version sort
# (order of these options is not important)
cat reference-sorted.txt|sort -dV > coreutils-sort-dict-version.txt
# diff
diff -Nup reference-sorted.txt coreutils-sort.txt > coreutils-sort.diff
diff -Nup reference-sorted.txt coreutils-sort-dict.txt > coreutils-sort-dict.diff
diff -Nup reference-sorted.txt coreutils-sort-version.txt > coreutils-sort-version.diff
diff -Nup reference-sorted.txt coreutils-sort-dict-version.txt > coreutils-sort-dict-version.diff
