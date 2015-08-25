#!/usr/bin/env python3

from wsgiref.simple_server import make_server
from webob import Request
# from cgi import escape
import locale
# import os
import re
# import sys


conversion = {
    'α': 'ḁ',
    'β': 'ḇ',
    'χ': 'ƈ',
    'δ': 'ɖ',
    'Δ': 'Ḏ',
    'ε': 'ḙ',
    'η': 'ḛ',
    'φ': 'ḟ',
    'Φ': 'Ḟ',
    'γ': 'ɠ',
    'Γ': 'Ɠ',
    'ι': 'ḭ',
    'κ': 'ƙ',
    'λ': 'ḻ',
    'Λ': 'Ḻ',
    'µ': 'ṃ',
    'ν': 'ŋ',
    'ω': 'ọ',
    'Ω': 'Ọ',
    'π': 'ṕ',
    'Π': 'Ṕ',
    'ψ': 'ṗ',
    'Ψ': 'Ṗ',
    'ρ': 'ṟ',
    'σ': 'ṣ',
    'ς': 'ṩ',
    'Σ': 'Ṣ',
    'τ': 'ṱ',
    'θ': 'ṯ',
    'Θ': 'Ṯ',
    'υ': 'ṵ',
    'ξ': 'ȥ',
    'Ξ': 'Ȥ',
    'ζ': 'ȥ',
}


def exact_conversion():
    substitute = {}
    restore = {}
    for char in conversion.keys():
        substitute[conversion[char]] = re.compile('{}'.format(char))
        restore[char] = re.compile('{}'.format(conversion[char]))

    return (substitute, restore)


def detail_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    html = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Woorden alfabetisch sorteren - OpenTaal</title>
    <link rel="stylesheet" href="jquery.mobile-1.4.5.min.css">
    <link rel="stylesheet" href="opentaal.css">
    <link rel="icon" href="favicon.ico" />
    <script src="jquery-2.1.4.min.js"></script>
    <script src="jquery.mobile-1.4.5.min.js"></script>
</head>
<body>
<div data-role="page">
<div data-role="header" class="jqm-header">
    <h1>Woorden alfabetisch sorteren - OpenTaal</h1>
</div><!-- /header -->

<div role="main" class="ui-content jqm-content">
<div class="ui-body-d ui-content">


'''

    words = '''BB
zo-even
C 32
sint-bernardshond
Sint-Maarten
B&B
smorgasbord
vri
smörgasbord
aanw. vnw.
α
cijfer- en letterwoorden
senor
C-32
call-out
A
Bonaire, Sint-Eustatius en Saba
S.
vry
I/O
ij-ligatuur
ysvogel
Bløf
vrj
klaar
Åland
2D-projecties
a-
IJsvogel
tv
bètastraling
ångström
α-deeltje
π-dag
Σ-regel
ct
micronano
χ²-toets
Slotervaart-Overtoomse Veld
C-31
een
C32
CO2-emissie
kilometer
P
d.d.
smorgåsbord
Giessendam/Neder-Hardinxveld
NOCNSF
Curaçao
11ᵉ Sweelinckstraat
2D-projectie
CD&V'er
µm
65+-kaart
m
bestand.txt
letterwoorden
curaçao
á
Slotervaart/Overtoomse/Veld
12ᵉ Sweelinckstraat
a.
100 eurobiljet
bestand12.txt
BLOF
50 eurobiljet
ijsvogel
A.
's avonds
sigmaregel
'14-'18
3D-projectie
bestand2.txt
π²
micrometer
Ijsvogel
ik
bestand-backup.txt
10ᵉ Sweelinckstraat
16 m²
16m²
l-calculus
iglo
C 31
Curacao
s-regel
λ-calculus
m2
3VO
cijfer
a
'40-'45
Bonaire, Sint-Eustatius & Saba
65-kaart
chi-kwadraattoets
Slotervaart Overtoomse Veld
bijectie
alfadeeltje
Slotervaart/Overtoomse-Veld
bijna
DDT
aug.
ca.
NOC*NSF
10 eurobiljet
A4
3D-projecties
Slotervaart/Overtoomse Veld
65+'er
ā
aub
callout
NOC NSF
input/output
π
CA
vrij
2ᵉ Sweelinckstraat
NOC-NSF
m²
Å
augustus
BLØF
C31
smörgåsbord
C&A
µ
pi
γ-straling
AA
tv's
zgn.
zoeven
k/h
à
cijfer-
lambdacalculus
één
NOC/NSF
m³
señor
c.i.a.
vrk
curacao
β-straling
km/s
Ysvogel
s
call out
gammastraling
's-Hertogenbosch
Blof
a-deeltje
m3
St.-Maarten
c.t.
CO₂-emissie
ä
St.-Eustatius
's ochtends
â
1ᵉ Sweelinckstraat
a.u.b.
å'''

    noliga = '-o-font-feature-settings: "liga" off; ' \
        '-o-font-variant-ligatures: none; ' \
        '-moz-font-feature-settings: "liga" off; ' \
        '-moz-font-variant-ligatures: none; ' \
        '-webkit-font-feature-settings: "liga" off; ' \
        '-webkit-font-variant-ligatures: none; ' \
        'font-feature-settings: "liga" off; ' \
        'font-variant-ligatures: none; '
    monospace = 'font-family: courier; ' + noliga
    # FIXME generic-family:monospace
    fullwidth = monospace + 'width: 100%; white-space: pre; '
    # FIXME nowrap ♥ chrome and pre ♥ firefox

    direction = 'Oplopend'
    order = 'Normaal'
    exact = 'Exact'
    forbiddenCharacters = []
    word_list = []
    if environ['REQUEST_METHOD'] == 'POST':
        req = Request(environ)
# word = unicode(req.params.get('name', 'default')).encode('utf-8') ##
# escape(...)
        direction = req.params.get('direction', '').strip()
        order = req.params.get('order', '').strip()
        exact = req.params.get('exact', '').strip()
        substitute = None
        restore = None
        if exact == 'Exact':
            (substitute, restore) = exact_conversion()
        words = req.params.get('words', '').strip()
        for word in words.split('\n'):
            if word != '':
                if exact == 'Exact':
                    for character in conversion.values():
                        if character in word:
                            if character not in forbiddenCharacters:
                                forbiddenCharacters.append(character)
                    for repl in substitute.keys():
                        word = re.sub(substitute[repl], repl, word)
                if order == 'Retrograad':
                    word = word[::-1]
                word_list.append(word)
        if len(forbiddenCharacters) == 0:
            try:
                locale.setlocale(locale.LC_ALL, "nl_NL.UTF-8")
            except locale.Error:
                try:
                    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
                except locale.Error:
                    try:
                        locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")
                    except locale.Error:
                        pass

            if direction == 'Aflopend':
                word_list = sorted(word_list, key=locale.strxfrm, reverse=True)
            else:
                word_list = sorted(word_list, key=locale.strxfrm)
            words = ''
            for word in word_list:
                if exact == 'Exact':
                    for repl in restore.keys():
                        word = re.sub(restore[repl], repl, word)
                if order == 'Retrograad':
                    word = word[::-1]
                    fullwidth += 'text-align: right; '
                words += '{}\n'.format(word)
            words = words[:-1]

    html += '<form action="sort.wsgi" data-ajax="false" id="sort" method="post">\n'
    html += '<input value="Sorteer" type="submit" data-icon="refresh"/>\n'
    if direction == 'Oplopend':
        html += '<select data-role="flipswitch" name="direction" ' \
                'data-wrapper-class="custom-size-flipswitch">' \
                '<option selected="">Oplopend</option>' \
                '<option>Aflopend</option>' \
                '</select>\n'
    else:
        html += '<select data-role="flipswitch" name="direction" ' \
                'data-wrapper-class="custom-size-flipswitch">' \
                '<option>Oplopend</option>' \
                '<option selected="">Aflopend</option>' \
                '</select>\n'
    if order == 'Normaal':
        html += '<select data-role="flipswitch" name="order" ' \
                'data-wrapper-class="custom-size-flipswitch">' \
                '<option selected="">Normaal</option>' \
                '<option>Retrograad</option>' \
                '</select>\n'
    else:
        html += '<select data-role="flipswitch" name="order" ' \
                'data-wrapper-class="custom-size-flipswitch">' \
                '<option>Normaal</option>' \
                '<option selected="">Retrograad</option>' \
                '</select>\n'
    if exact == 'Exact':
        html += '<select data-role="flipswitch" name="exact" ' \
                'data-wrapper-class="custom-size-flipswitch">' \
                '<option selected="">Exact</option>' \
                '<option>Standaard</option>' \
                '</select>\n'
    else:
        html += '<select data-role="flipswitch" name="exact" ' \
                'data-wrapper-class="custom-size-flipswitch">' \
                '<option>Exact</option>' \
                '<option selected="">Standaard</option>' \
                '</select>\n'
    html += '</form>\n'

    if len(forbiddenCharacters) != 0:
        html += '<div class="ui-nodisc-icon"><a href="index.html" class="ui-btn ui-shadow ui-corner-all ui-icon-alert ui-btn-icon-notext ui-btn-b ui-btn-inline">Waarschuwing:</a> De karaters {} zijn niet toegestaan bij Exact sorteren. Er heeft geen sortering plaatsgevonden!</div>'.format(', '.join(forbiddenCharacters))

    html += '<textarea style=\'{}\' name="words" rows="8" placeholder="maan\nroos\nvis" form="sort">{}' \
        '</textarea>\n'.format(fullwidth, words)#placeholder new line werkt niet op firefix, wel chrome

    html += '''<br/>
    <div data-role="collapsible-set">'''
    html += '''
        <div data-role="collapsible" data-collapsed-icon="carat-r"
        data-expanded-icon="carat-d" data-mini="true" data-collapsed="true">
            <h2>Gebruik</h2>
            <small>
            <p>Deze webinterface biedt een praktische manier om woorden
            alfabetisch te sorteren. Het doel hiervan is een sortering te
            kunnen maken voor gebruik in woordenlijsten en  woordenboeken.</p>
            <p>De eerste optie Oplopend/Aflopend is triviaal. De tweede optie
            Normaal/Retrograad sorteert vanaf de achterkant van het woord naar
            de voorkant als voor Retrograad is gekozen. Dat is handig voor het
            groeperen van bepaalde uitgangen. Om die reden is resultaat van
            retrograad sorteren rechts uitgelijnd. De derde optie Exact/Normaal
            zal als voor Exact is gekozen Griekse letters zoals in woorden als
            µm en λ-calculus op uitspraak alfabetisch sorteren. Normaal doet
            het sorteeralgoritme dit niet en komen deze woorden meestal
            helemaal op het einde te staan.</p>
            <p>Indien voor Exact is gekozen mogen de karakters {} niet
            voorkomen in de woorden die gesorteerd worden. Deze worden tijdens
            het sorteren tijdelijk gebruikt voor de ondersteuning van Griekse
            letters. Als deze toch in de te sorteren woorden zijn gebruikt zal
            daarvoor gewaarschuwd worden. Indien andere karakters hiervoor
            nodig zijn kan dat worden doorgegeven via GitHub.</p>
            <img src="logos/opentaal-256.png" alt="Logo Stichting OpenTaal">
            <p>De aangeboden sortering komt voort uit een onderzoeksproject van
            Stichting OpenTaal dat is uitgevoerd in samenwerking met de
            Nederlandse Taalunie. Voor achtergrondinformatie, details en
            overwegingen, zie <a target="_blank"
            href="https://github.com/OpenTaal/alphabetical-sort">
            alphabetical-sort</a> op GitHub.</p>
            <p>Neem contact op met Stichting OpenTaal als u behoefte hebt aan
            een maatwerk sortering. Die kan door onze <a target="_blank"
            href="http://opentaal.org/vrienden-van-opentaal">officiële
            partners</a> worden vervaardigd.</p>
            </small>
        </div>
        <div data-role="collapsible" data-collapsed-icon="carat-r"
        data-expanded-icon="carat-d" data-mini="true" data-collapsed="true">
            <h2>Colofon</h2>
            <small>
            <p>Het ontwerp en de ontwikkeling van deze sorteerinterface is
            mogelijk gemaakt door <a target="_blank"
            href="http://hellebaard.nl">Hellebaard</a>, een officiële partner
            van Stichting OpenTaal.</p>
            <p>Volg <a target="_blank" href="http://opentaal.org">Stichting
            OpenTaal</a> ook op
            <a target="_blank" href="http://twitter.com/OpenTaal">Twitter</a>,
            <a target="_blank"
            href="http://linkedin.com/company/stichting-opentaal">LinkedIn</a>,
            <a target="_blank" href="http://facebook.com/opentaal">Facebook</a>
            , <a target="_blank" href="http://google.com/+OpentaalOrg">
            Google+</a> en op onze eigen <a target="_blank"
            href="http://lists.sf.own-it.nl/pipermail/opentaal/">mailinglijst
            </a>.</p>
            </small>
        </div>
    </div>
</div><!-- /word -->
</div><!-- /main -->
</div><!-- /page -->
</body>
</html>'''.format(', '.join(sorted(conversion.values())))
    return [html.encode('utf-8')]


def application(environ, start_response):
    return detail_app(environ, start_response)


if __name__ == '__main__':
    httpd = make_server('', 8000, detail_app)
    print("Serving on port 8000...")
    httpd.serve_forever()
