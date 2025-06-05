Some helpful stuff for displaying song chords (or just the bare chords) for string instruments.

## Printing chords

A chord can be defined like so:

```python
from chordist.banjo import BanjoChord

em = BanjoChord.create("Em", (2, 1, 2), (2, 4, 3))
g = BanjoChord.create("G")
```

... where the arguments to `BanjoChord.create()` are the chord name followed by a tuple in the format `(fret number, string number, [finger number])` for each pressed string. String numbers are counted from the top/left, which I am sure somebody will take issue with (feel free to change this in your own fork in that case). The finger number can be omitted, in which case a `*` will be used. It can also be a string, for example `x` for muted strings.

To output the chords above:

```python
from chordist.instrument_chord import InstrumentChordCollection

chords = InstrumentChordCollection(em, g)
chords.print_matrix()
```

This prints:

```
__Em___       ___G___
| | | |       | | | |
2 | | 3       | | | |
| | | |       | | | |
| | | |       | | | |
```

To print all predefined chords, just do:

```python
from chordist.banjo import BASE_CHORDS

BASE_CHORDS.print_matrix()
```

For guitar chords, just use `chordist.guitar.GuitarChord` and `chordist.guitar.BASE_CHORDS` instead.

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
from chordist.banjo import BASE_CHORDS
from chordist.song import Song

rows = lyrics.split("\n")  # lyrics = the above stuff as a string
song = Song.create(lyrics=rows, chords=BASE_CHORDS, title="Roll in My Sweet Baby's Arms")
song.print()
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

___G___       __D⁷___       ___C___       ___C___          C
| | | |       | | 1 |       | | 1 |       | | 1 |       1 1 1 1 5fr
| | | |       | 2 | |       | | | 2       2 | | 3       | | | |
| | | |       | | | |       | | | |       | | | |       | | | |
| | | |       | | | 4       | | | |       | | | |       | | | |
```

(There are 3 variations of the C chord among the base banjo chords. To only print the first variation, run `song.print(variations=False)`.)

## Transposing

Various objects can be transposed. Example using the song from above:

```python
song.transpose(2).print(variations=False)  # Up two half notes
```

Output:
```
Roll in My Sweet Baby's Arms
============================

A
Roll in my sweet baby's arms
                        E⁷
Roll in my sweet baby's arms
      A
Gonna lay around the shack
         D
'Til the mail train comes back
    E⁷                      A
And roll in my sweet baby's arms

___A___       __E⁷___       ___D___
| | | |       | 1 | |       | | | |
1 1 1 1       2 | | |       | 1 | |
| | | |       | | | |       | | 2 |
| | | |       | | | |       | | | 3
```

## Bugs/caveats

Not yet able to render the high G string on a 5-string banjo in any useful way.
