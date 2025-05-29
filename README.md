Some helpful stuff for displaying song chords (or just the bare chords) for string instruments.

## Printing chords

A chord can be defined like so:

```python
from chordist.banjo import BanjoChord

em = BanjoChord("Em", (2, 1, 2), (2, 4, 3))
g = BanjoChord("G")
```

... where the arguments to `BanjoChord` are the chord name followed by a tuple in the format `(fret number, string number, [finger number])` for each pressed string. The finger number can be omitted, in which case a `*` will be used. It can also be a string, for example `x` for muted strings.

To output the chords above:

```python
from chordist.banjo import Banjo

banjo = Banjo([em, g])
banjo.print_chord_matrix(["Em", "G"])
```

This prints:

```
__Em___      ___G___
| | | |      | | | |
2 | | 3      | | | |
| | | |      | | | |
| | | |      | | | |
```

To print all predefined chords, just do `banjo.print_chord_matrix()`.

For guitar chords, just use `chordist.guitar.GuitarChord` and `chordist.guitar.Guitar` instead.

## Lyrics

Let's say we have a piece of lyrics with inlined chords, in this format:

```
[G]Roll in my sweet baby's arms
Roll in my sweet baby's [D7]arms
Gonna [G]lay around the shack
'Til the [C]mail train comes back
And [D7]roll in my sweet baby's [G]arms
```

Here is how we can format them a bit nicer and also print the relevant banjo chords:

```python
from chordist.banjo import Banjo

banjo = Banjo()
chorus = lyrics.split("\n")  # lyrics = the above stuff as a string
banjo.print_lyrics(chorus, title="Roll in My Sweet Baby's Arms")
```

Output:

```
Roll in My Sweet Baby's Arms
============================

G
Roll in my sweet baby's arms
                        D⁷
Roll in my sweet baby's arms
      G
Gonna lay around the shack
         C
'Til the mail train comes back
    D⁷                      G
And roll in my sweet baby's arms

___G___      __D⁷___      ___C___
| | | |      | | 1 |      | | 1 |
| | | |      | 2 | |      2 | | 3
| | | |      | | | |      | | | |
| | | |      | | | 4      | | | |
```

`print_lyrics()` also accepts an iterable of string iterables, in which case the outer iterables will be treated as separate verses and separated by blank rows.

Some more examples in `abstract_instrument.py`.

## Bugs/caveats

Not yet able to render the high G string on a 5-string banjo in any useful way.
