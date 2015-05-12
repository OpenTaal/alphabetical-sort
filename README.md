# alphabetical-sort


## Introduction

Visually looking up words in a large dictionary, glossary or index can be done
efficiently when these are ordered in an alphabetical way. Likewise, a dozen
suggestions offered by autocompletion are effective when the lexicographical
ordering places related words near each other.

To sort alphabetically in a practical language-specific way is however far from
trivial. This is in particular when numerals, spaces, hyphens, special
characters and diacritical marks need to be taken into account. Additionally, different regional conventions exist when ordering diacritics, capitals and
proper names.

A simple alphabetic sorting provided by most programming languages is unsuitable
for this purpose. As will be demonstrated, sorting a well-constructed reference
list will, firstly, document specific ordering requirements, and secondly, give
insight to existing sorting algorithms.

The aim in this project is not to develop a custom algotihm necessarily. Using
an existing standard sollution will be aimed for as much as possible for reasons
of compatability and maintainability. Hence, allowing minor changes in the
requirements when needed to keep this approach.

This project offers a test-driven selection and customisation of an
alphabetical sorting algorithm, primarily aimed at the Dutch language. The joint
effort of computational linguistics, lexicographers and language enthousiasts
is reflected in the result of this project. This project is offered under an MIT
license. Any external software used falls naturally under their respective
licenses.


## Problem

Default sort algorithm on most operating systems, especially UNIX-bases systems,
will use the sort order as defined in the locale. For most Western locales, such
as English, Dutch and German, the sort order is defined in the locale
[iso14651_t1_common](http://sourceware.org/git/?p=glibc.git;a=blob;f=localedata/locales/iso14651_t1_common;hb=HEAD). This and other locale definitions are part of
the GNU C Library also known as glibc.

The command-line tool
[sort](http://en.wikipedia.org/wiki/Sort_%28Unix%29) from the coreutils package
uses this localised sort order. However, when sorting the reference set for this project,
[reference-sorted.txt](https://github.com/OpenTaal/alphabetical-sort/blob/master/reference-sorted.txt), one of the results the results are satisfactory.

When it is used for default sorting, the result is [coreutils-sort.txt](https://github.com/OpenTaal/alphabetical-sort/blob/master/coreutils-sort.txt) and the difference with the reference is [coreutils-sort.diff](https://github.com/OpenTaal/alphabetical-sort/blob/master/coreutils-sort.diff). Note TODO (that sort places 100 before 10 and interchanges smorgåsbord with smörgåsbord.)

When it is used for sorting in dictionary order, considering only blanks and alphanumeric characters, the result is [coreutils-sort-dictionary.txt](https://github.com/OpenTaal/alphabetical-sort/blob/master/coreutils-sort-dictionary.txt) and the difference with the reference is [coreutils-sort-dictionary.diff](https://github.com/OpenTaal/alphabetical-sort/blob/master/coreutils-sort-dictionary.diff). Note that characters with diacritics are not ordered as desired.

When it is used for sorting in version order, natural sort of (version) numbers within text, the result is [coreutils-sort-version.txt](https://github.com/OpenTaal/alphabetical-sort/blob/master/coreutils-sort-version.txt) and the difference with the reference is [coreutils-sort-version.diff](https://github.com/OpenTaal/alphabetical-sort/blob/master/coreutils-sort-version.diff). Note TODO.

When dictionary order and version order are used at the same time, the order of these options is not important, the result is [coreutils-sort-dictionary-version.txt](https://github.com/OpenTaal/alphabetical-sort/blob/master/coreutils-sort-dictionary-version.txt) and the difference with the reference is [coreutils-sort-dictionary-version.diff](https://github.com/OpenTaal/alphabetical-sort/blob/master/coreutils-sort-dictionary-version.diff). Note issues from dictionary order are again preventing to match the sort with the reference set.

TODO add example with python default sort and with python locale sort


## Requirements

Requirements for developing an algorith which sorts alphabetically in a
language-specific way for lexicographical purposes are:
* Sorting must respect an ascending alphabetical order.
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
* Sorting of mathemathical, chemical and other symbols such as Greek characters
  must be done in a predefined order.
* Sorting of characters for which no order is provided must be done after all
  defined characters in order of default alphabetical sorting provided by the
  programming language.
* Software must be developed in a test-driven way.
* Sorting must be done according to predfined ordered list of characters and
  words. These can be found in
  [references/sort-characters.txt](https://github.com/OpenTaal/alphabetical-sort/blob/master/references/sort-characters.txt)
  which is generated from [references/sort-characters.tsv](https://github.com/OpenTaal/alphabetical-sort/blob/master/references/sort-characters.tsv)
  and
  [references/sort.txt](https://github.com/OpenTaal/alphabetical-sort/blob/master/references/sort.txt)
  which is generated from [references/sort.tsv](https://github.com/OpenTaal/alphabetical-sort/blob/master/references/sort.tsv)
* Sorting must be possible in descending or reverse alphabetical order as is
  defined in
  [references/sort-reverse.txt](https://github.com/OpenTaal/alphabetical-sort/blob/master/references/sort-reverse.txt)
* Sorting must be possible in retrograde alphabetical order as is defined in
  [references/sort-retrograde.txt](https://github.com/OpenTaal/alphabetical-sort/blob/master/references/sort-retrograde.txt)
* Sorting must be possible in reverse retrograde alphabetical order as is
  defined in
  [references/sort-retrograde-reverse.txt](https://github.com/OpenTaal/alphabetical-sort/blob/master/references/sort-retrograde-reverse.txt)
* Sorting must be optimsed, however a two-pass sorting is allowed when needed.

Requirements which are out of scope are:
* sorteren op achternaam
* letterwoorden vooraan
*
*

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
* [msort](http://billposer.org/Software/msort.html)
* http://icu-project.org/icu-bin/locexp?_=en_US&x=col
* [English locale for the Netherlands](https://github.com/PanderMusubi/locale-en-nl/blob/master/en_NL)
* [Number forms](https://en.wikipedia.org/wiki/Number_Forms)

Ses also on sorting in Dutch:
* [Alfabetische volgorde](http://nl.wikipedia.org/wiki/Alfabetische_volgorde)
* [Retrograad sorteren](http://nl.wikipedia.org/wiki/Retrograad_(woordenlijst))

See also on sorting in German:
* [Sorting German sharp s](http://faql.de/eszett.html)

TODO:
* https://sf.own-it.nl/projects/opentaal/wiki/Karakters
* https://sf.own-it.nl/projects/opentaal/wiki/Sorteren
