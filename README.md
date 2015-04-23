# alphabetical-sort

Visually looking up words in an alphabetically sorted word list or dictionary
requires a practical sorting algorithm. However, to sort alphabetically in a
language-specific way for lexicographical purposes is far from trivial when
special characters and diacritical marks need to be taken into account.

Standard alphabetic sorting provided by programming languages is not suitable
for purpose, even when localised sorting is enabled. A custom sorting algorithm
is needed to solve this problem. This project offers the test-driven development
of such alphabetical sorting algorithm by a community of computational
linguistics and offers the implementation under an MIT license.

The implementation is in Python but code from this project can be used as a
reference for implementations in other programming languages. At the moment only
Dutch (nl) is supported.

Requirements for developing an algorith which sorts alphabetically in a
language-specific way for lexicographical purposes are:
* Sorting must respect the alphabetical order.
* Sorting is unaware if it processes a normal word or an abbreviation.
* Sorting algorithm must group lower and upper case of the same character with
  priority for the lower case character.
* Sorting must group word characters and prioritise according to
  ampersand, slash, comma, space, period, apostroph and hyphen.
* Sorting must group characters without and with diacritics and
  prioritise first to character case and secondly to a predefined order.
* Sorting must group numerals in numerical ascending way and
  prioritise these according to superscipt, subscript and the default
  representation.
* Sorting of mathemathical, chemical and other symbols must be done in a
  predefined order.
* Sorting of characters for which no order is provided must be done after all
  defined characters in order of default alphabetical sorting provided by the
  programming language.
* Sorting must be alphabetically ascending. The reference sorted word list is
  https://github.com/OpenTaal/alphabetical-sort/blob/master/reference-sorted.txt
* Sorting can be alphabetically descending. The reference reverse sorted word
  list is
  https://github.com/OpenTaal/alphabetical-sort/blob/master/reference-sorted-reverse.txt
* Sorting can be retrograde alphabetically ascending. The reference retrograde
  sorted word list is
  https://github.com/OpenTaal/alphabetical-sort/blob/master/reference-sorted-retrograde.txt
* Sorting can be retrograde alphabetically descending. The reference reverse
  retrograde sorted word list is
  https://github.com/OpenTaal/alphabetical-sort/blob/master/reference-sorted-reverse-retrograde.txt
* Software must be developed in a test-driven way. The script to run the unit
  tests is https://github.com/OpenTaal/alphabetical-sort/blob/master/test.py
* Sorting must be done according to a predefined ordered list of characters. The
  list can be found in
  https://github.com/OpenTaal/alphabetical-sort/blob/master/sort-order.tsv
* Sorting must be optimsed, however a two-pass sorting is allowed. The algorithm
  is implemented in
  https://github.com/OpenTaal/alphabetical-sort/blob/master/asort.py

See also on sorting:
* English:
  * http://en.wikipedia.org/wiki/Alphabetical_order
  * http://en.wikipedia.org/wiki/Rhyming_dictionary
  * http://en.wikipedia.org/wiki/Unicode_collation_algorithm
  * http://en.wikipedia.org/wiki/ISO_14651
  * http://en.wikipedia.org/wiki/European_ordering_rules
  * http://collation-charts.org
  * http://unicode.org/reports/tr10
  * http://developer.mimer.com/collations
  * http://developer.mimer.com/charts
  * http://billposer.org/Software/msort.html
  * http://sourceware.org/git/?p=glibc.git;a=blob;f=localedata/locales/iso14651_t1;hb=HEAD
  * http://sourceware.org/git/?p=glibc.git;a=blob;f=localedata/locales/iso14651_t1_common;hb=HEAD
  * http://icu-project.org/icu-bin/locexp?_=en_US&x=col
  * https://github.com/PanderMusubi/locale-en-nl/blob/master/en_NL
* Dutch:
  * http://nl.wikipedia.org/wiki/Alfabetische_volgorde
  * http://nl.wikipedia.org/wiki/Retrograad_(woordenlijst)
