# alphabetical-sort

## Introduction

Visually looking up words in an alphabetically sorted word list or dictionary
requires a practical sorting algorithm. However, to sort alphabetically in a
language-specific way for lexicographical purposes is far from trivial,
in particular when special characters and diacritical marks need to be taken
into account.

Standard alphabetic sorting provided by programming languages is not suitable
for this purpose, even when a localised sorting is enabled. It will be
demonstrated that a custom sorting algorithm is needed to solve this problem
when sorting for example for the Dutch language.

This project offers the test-driven development of such alphabetical sorting
algorithm by a community of computational linguistics and offers the
implementation under an MIT license.

The implementation of the alphabetical sorting algorith delivered by this
project can be used directly in the provided implementation. Additionally, this
implementation can also be used as a reference for implementations the algorithm
in other programming languages. At the moment only Dutch (nl) is supported.

## Problem
Default sort algorithm on most operating systems, especially UNIX-bases systems,
will use the sort order as defined in the locale. For most Western locales such
as English, Dutch and German, the sort order is defined in the locale
[iso14651_t1_common](http://sourceware.org/git/?p=glibc.git;a=blob;f=localedata/locales/iso14651_t1_common;hb=HEAD) of the GNU C Library also known as glibc. The command-line tool [sort](http://en.wikipedia.org/wiki/Sort_%28Unix%29) from the coreutils package uses this localised sort order. However, when sorting the reference set for this project,
[reference-sorted.txt](https://github.com/OpenTaal/alphabetical-sort/blob/master/reference-sorted.txt), one of the results the results are satisfactory.

When it is used for default sorting, the result is [coreutils-sort.txt](https://github.com/OpenTaal/alphabetical-sort/blob/master/coreutils-sort.txt) and the difference with the reference is [coreutils-sort.diff](https://github.com/OpenTaal/alphabetical-sort/blob/master/coreutils-sort.diff). Note TODO (that sort places 100 before 10 and interchanges smorgåsbord with smörgåsbord.)

When it is used for sorting in dictionary order, considering only blanks and alphanumeric characters, the result is [coreutils-sort-dictionary.txt](https://github.com/OpenTaal/alphabetical-sort/blob/master/coreutils-sort-dictionary.txt) and the difference with the reference is [coreutils-sort-dictionary.diff](https://github.com/OpenTaal/alphabetical-sort/blob/master/coreutils-sort-dictionary.diff). Note that characters with diacritics are not ordered as desired.

When it is used for sorting in version order, natural sort of (version) numbers within text, the result is [coreutils-sort-version.txt](https://github.com/OpenTaal/alphabetical-sort/blob/master/coreutils-sort-version.txt) and the difference with the reference is [coreutils-sort-version.diff](https://github.com/OpenTaal/alphabetical-sort/blob/master/coreutils-sort-version.diff). Note TODO.

When dictionary order and version order are used at the same time, the order of these options is not important, the result is [coreutils-sort-dictionary-version.txt](https://github.com/OpenTaal/alphabetical-sort/blob/master/coreutils-sort-dictionary-version.txt) and the difference with the reference is [coreutils-sort-dictionary-version.diff](https://github.com/OpenTaal/alphabetical-sort/blob/master/coreutils-sort-dictionary-version.diff). Note issues from dictionary order are again preventing to match the sort with the reference set.

TODO add example with python default sort and with python locale sort


## Requirements

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
*
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

## Further reading

See also on sorting in English:
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
* http://icu-project.org/icu-bin/locexp?_=en_US&x=col
* https://github.com/PanderMusubi/locale-en-nl/blob/master/en_NL

Ses also on sorting in Dutch:
* http://nl.wikipedia.org/wiki/Alfabetische_volgorde
* http://nl.wikipedia.org/wiki/Retrograad_(woordenlijst)

See also on sorting in German:
* http://faql.de/eszett.html
