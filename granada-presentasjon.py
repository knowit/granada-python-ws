# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Grunnleggende syntaks og data-typer
# ========================
# 
# Under følger en demo av grunnleggende Python. Alle eksemplene kan puttes i egne filer og kjøres derfra eller de kan tastes inn i en interpreter som kjøres med `$ python`.
# 
# Komplett program (helloworld.py):
# =================

# <codecell>

print("Hello, World!")

# <markdowncell>

# Kan lagres til helloworld.py og kjøres med:
# 
# `$ python helloworld.py`

# <markdowncell>

# Komplett program (echo.py):
# =========================
# 
# Imports i python er rett frem, kan gjøres på flere forskjellige måter. Vi bruker .-operator for å hente objekter ut av moduler:

# <codecell>

import sys

program_name = sys.argv[0]
arguments = sys.argv[1:]
print(' '.join(arguments))

from sys import argv
print('\n'.join(argv))

# <markdowncell>

# Her skjer det mye. Vi noterer oss:
# 
# - `import navn` gjør at vi kan referer til `navn.ting` for å gjenbruke modulen `navn`
# - `from navn import ting` gjør at vi kan refere til `ting`
# - `sys.argv` er en list; `[]` er indexing operator
# - eksempel på slicing, `sys.argv[1:]` betyr "fra og med element med index 1"
# - join er en metode eid av str, i python heter det `delimiter.join(things)` og join kan bruke en iterable (list, dict, tuple, str, ...)
# 
# Hvordan finne slike ting?
# ```
# >>> from sys import argv
# >>> help(argv)
# ```

# <codecell>

from os import path
help(path)

# <markdowncell>

# Kan også bruke `help()` uten argumenter for interaktiv hjelp.

# <markdowncell>

# Funksjoner
# ==========
# 
# Funksjoner introduseres ved å bruke `def navn(parameterliste):`. Fordi indentering er obligatorisk i Python kan man ikke ha en funksjon med "tom" kropp, konvensjonen er å bruke `pass` som placeholder eller å skrive en doc-string. Man indenterer med 4 spaces:

# <codecell>

def is_type(thing):
    """This is a doc-string, it is used to generate documentation and provide help()"""
    return isinstance(thing, type)
print('is_type(int) == {}'.format(is_type(int)))
help(is_type)

# <markdowncell>

# `help()` er faktisk bare en noe komplisert funksjon som bruker introspection for å vise hva ting gjør:

# <codecell>

print(is_type.__doc__)
print(dir(list))
print(list.__str__.__doc__)

# <markdowncell>

# Datatyper
# =========
# 
# Følgende er de mest sentrale datatypene i Python:
# 
# - str (unicode-streng i python3, bytestring i python2)
# - bool, int, float
# - list (tenk ArrayList, ikke LinkedList)
# - tuple (immutable sequence)
# - set (tenk HashSet)
# - dict (tenk HashMap eller HashTable)
# 
# Alle disse har syntaks:

# <codecell>

name = "Robin"
is_cool = True
age = 27
distance_in_km = 913.2
to_do = ['Code', 'Eat', 'Sleep'] # eller list(iterable)
plan = ('Present', 'Help') # eller tuple(iterable)
users = {'Robin', 'Øyvind'} # eller set(iterable)
coolness = {'Robin': 1337, 'Øyvind': 1336} # eller dict(iterable_of_pairs)

print(age / distance_in_km)
print(to_do[0:2])
print(name in users)
print(coolness['Øyvind'])
# KeyError:
# print(coolness['Not cool'])
# Default til 0 dersom ikke kul:
print(coolness.get('Not cool', 0))
coolness['Not cool'] = coolness.get('Not cool', 0) + 1
print(coolness)

# <markdowncell>

# Minner på `help({})` f. eks.
# 
# Det finnes i tillegg mange nyttige datatyper i standard-biblioteket, noen av de vi bruker mest:
# 
# - `collections.namedtuple`:

# <codecell>

from collections import namedtuple
Failure = namedtuple('Failure', ['status_code', 'reason'])
proxy_error = Failure(502, 'Proxy Error: Bad Gateway')
print(proxy_error)
print(proxy_error.status_code)
print(proxy_error.reason)
# Immutable, kan ikke gjøre dette:
# proxy_error.status_code = 404

# <markdowncell>

# - `collections.Counter`:

# <codecell>

from collections import Counter
print(Counter("foobar"))
print(Counter([1, 2, 3, 1, 1, 9]))

# <markdowncell>

# - `collections.OrderedDict` når rekkefølge har betydning:

# <codecell>

pairs = [("a", 9), ("b", 13), ("foo", 17), ("bar", 37), ("c", 7)]
print(dict(pairs)) # Abitrær rekkefølge
from collections import OrderedDict
print(OrderedDict(pairs)) # Bestemt rekkefølge

# <markdowncell>

# - `collections.defaultdict` for f. eks. å defaulte til tom liste:

# <codecell>

from collections import defaultdict
cool_things_about_people = defaultdict(list)
print(cool_things_about_people['Robin'])

# <markdowncell>

# Løkker, ifs og sånn
# ===================
# 
# I Python har vi bare for-each løkker som ser slik ut:
# ```
# for element in iterable:
#     do_stuff_with(element)
# ```
# Vi har vanlig if-elif-else, men det er ikke bare False som evalueres som False i boolsk context. Ting som er Falsy:
# 
# - Tallet 0
# - En 'tom' ting (en iterable med lengde 0)
# - False
# - None (tilsvarer null)
# 
# Dersom du sammenlikner med `==` blir ikke ting gjort til bool, mao kan en str aldri `== True`. Du kan eksplisitt 'boolifisere' ting med `bool()`:

# <codecell>

print(bool('True'))
print(bool('foeuaeu'))

# <markdowncell>

# 'boolifisering' følger samme reglene som boolsk context (if, while og slikt).
# 
# Syntaks (vi putter ikke unødvendige parenteser rundt conditions i Python):

# <codecell>

x = 3
while x < 11:
    if 4 < x < 10:
        print('x between 4 and 10')
    elif x < 5:
        print('x is very small')
    else:
        print('ABORT ABORT')
    x += 1

# <markdowncell>

# Iterering
# ---------
# 
# Siden vi ikke har en tellende løkke i Python generer vi en iterable fra start til stop med `range(stop)` eller , `range(start, stop, [step])`:

# <codecell>

for i in range(10, 0, -1):
    print(i)

# <markdowncell>

# Men man trenger sjelden tellende løkker. Dersom du vil iterere over noe og du trenger indeksen bruker du iterator-apiet:

# <codecell>

for index, character in enumerate("foobar"):
    print('"foobar"[{index}] = "{character}"'.format(**locals()))

# <markdowncell>

# Dersom du må iterere over noe baklengs bruker du også iterator-apiet:

# <codecell>

for index, character in enumerate(reversed("foobar")):
    print('reversed("foobar")[{index}] = "{character}"'.format(**locals()))

# <markdowncell>

# Vi bruker også iterator-api for sortering med `sorted()`. Vi kan bruke `zip()` for å 'flette' to sekvenser:

# <codecell>

print(list(zip(range(10), "foobar")))

# <markdowncell>

# Comprehensions
# --------------
# 
# Veldig ofte når man itererer over noe er det for å bygge en data-struktur, f. eks. en Map, ArrayList eller HashSet. I Python har vi bruker man X comprehensions for x i (list, set, dict):

# <codecell>

doubled_odd_numbers = [x * 2 if x % 2 == 1 else x for x in range(20)]
double_only_evens = [x * 2 for x in range(20) if x % 2 == 0]
set_of_things = {x * 13 for x in [13, 13, 7, 12, 91]}
dict_of_indexes = {character: index for index, character in enumerate("foobar")}

# <markdowncell>

# Lambda og funksjonell programmering
# ===================================
# 
# Python har også lambda og closures. `lambda parameterliste: kropp` brukes for å introdusere en anonym funksjon -- anonyme funksjoner er begrenset til *ett* uttrykk og *en* linje i Python. Men man har altså mulighet til å bruke kjente funksjonelle idiomer som `map`, `filter` og `reduce` dersom det blir penere enn comprehensions eller løkker.

# <codecell>

for ordinal, character in zip(map(ord, 'foobar'), 'foobar'):
    print('ascii ordinal of {character} is {ordinal}'.format(**locals()))
from functools import reduce
print('Ordinal sum of "foobar" is: {}'.format(reduce(lambda x, y: x + ord(y), 'foobar', 0)))
# Men, mer idiomatisk:
print('Ordinal sum of "foobar" is: {}'.format(sum(ord(char) for char in 'foobar')))

# <markdowncell>

# Filer og slikt
# ===============
# 
# Man åpner filer ved å bruke `open(filsti, mode='r')` som returnerer en 'file-like'. Filer er iteratorer:

# <codecell>

code = open('data.py')
for line_no, line in enumerate(code):
    print(line_no, line, end='')

# <markdowncell>

# Man må jo egentlig også lukke filer, men det er litt plagsomt. I Python bruker vi 'context-managers' for resource-management. Da får vi et scope hvor ressursen er tilgjengelig, og så lukkes den automatisk etterpå:

# <codecell>

from collections import Counter
with open('data.py') as code:
    print(code.closed)
    print({word: count for word, count in Counter(word for word in code.read().split()).items() if count > 10})
    print(code.closed)
print(code.closed)

# <markdowncell>

# Tuples, unpacking, packing
# =========================
# 
# Python har en slags begrenset form for pattern matching slik alle kjenner det fra Haskell (ehh)

# <codecell>

x, y = [9, 8]
print(x, y)
x, y = y, x
print(x, y)

# <markdowncell>

# Under the hood gjøres dette med tuples og kalles unpacking dersom man assigner til flere verdier på venstre siden enn man har på høyre, og packing dersom motsatt.
# 
# Man kan også være mer avansert:

# <codecell>

x, *rest = "foobar"
print(x)
print(rest)

# <markdowncell>

# Her brukes `*` litt som i en regex eller glob, den sier 'resten'. *Enda* mer avansert bruk (gasp):

# <codecell>

first, *middle, last = range(20)
print(first)
print(middle)
print(last)

# <markdowncell>

# Keyword args, varargs, keyword varargs
# =================================
# 
# Man kan kalle funksjoner med keyword arguments i Python og man kan også angi default arguments:

# <codecell>

def fun(x, y=9):
    return x + y
print(fun(y=7, x=3))
print(fun(1))

# <markdowncell>

# Dersom man ønsker å tillatte varargs, kan man bruke tuple-unpacking syntaks men den fungerer motsatt. Argumentene blir pakket til en tuple:

# <codecell>

def fun(first, *rest):
    print(first)
    print(isinstance(rest, tuple))
    return sum(rest)
fun(9, 11, 7)

# <markdowncell>

# Det går også an å samle opp varargs for keywords:

# <codecell>

def fun(x, y, **others):
    mapping = {'x': x, 'y': y}
    mapping.update(others)
    return mapping
fun(4, 5, z=12)

# <codecell>


