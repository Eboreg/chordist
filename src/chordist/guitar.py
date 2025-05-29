from chordist.abstract_instrument import AbstractInstrument
from chordist.chord import Chord


class GuitarChord(Chord):
    def __init__(self, name, *fingers):
        super().__init__(name, 6, *fingers)


class Guitar(AbstractInstrument):
    string_count = 6
    chords = [
        GuitarChord("A", (1, 1, "x"), (2, 3, 1), (2, 4, 2), (2, 5, 3)),
        GuitarChord("A⁷", (1, 1, "x"), (2, 3, 1), (2, 5, 2)),
        GuitarChord("Am", (1, 1, "x"), (1, 5, 1), (2, 3, 2), (2, 4, 3)),
        GuitarChord("B", (1, 1, "x"), (2, 2, 1), (2, 6, 1), (4, 3, 2), (4, 4, 3), (4, 5, 4)),
        GuitarChord("B⁷", (1, 1, "x"), (1, 3, 1), (2, 2, 2), (2, 4, 3), (2, 6, 4)),
        GuitarChord("Bm", (1, 1, "x"), (2, 2, 1), (2, 6, 1), (3, 5, 2), (4, 3, 3), (4, 4, 4)),
        GuitarChord("C", (1, 1, "x"), (1, 5, 1), (2, 3, 2), (3, 2, 3)),
        GuitarChord("C⁷", (1, 1, "x"), (1, 5, 1), (2, 3, 2), (3, 2, 3), (3, 4, 4)),
        GuitarChord("Cm", (3, 1, "x"), (3, 2, 1), (3, 6, 1), (4, 5, 2), (5, 3, 3), (5, 4, 4)),
        GuitarChord("D", (1, 1, "x"), (1, 2, "x"), (2, 4, 1), (2, 6, 2), (3, 5, 3)),
        GuitarChord("D⁷", (1, 1, "x"), (1, 2, "x"), (1, 5, 1), (2, 4, 2), (2, 6, 3)),
        GuitarChord("Dm", (1, 1, "x"), (1, 2, "x"), (1, 6, 1), (2, 4, 2), (3, 5, 3)),
        GuitarChord("E", (1, 4, 1), (2, 2, 2), (2, 3, 3)),
        GuitarChord("E⁷", (1, 4, 1), (2, 2, 2)),
        GuitarChord("Em", (2, 2, 1), (2, 3, 2)),
        GuitarChord("F", (1, 1, "x"), (1, 2, "x"), (1, 5, 1), (1, 6, 1), (2, 4, 2), (3, 3, 3)),
        GuitarChord("F⁷", (1, 1, 1), (1, 3, 1), (1, 5, 1), (1, 6, 1), (2, 4, 2), (3, 2, 3)),
        GuitarChord("Fm", (1, 1, 1), (1, 4, 1), (1, 5, 1), (1, 6, 1), (3, 2, 3), (3, 3, 4)),
        GuitarChord("G", (2, 2, 1), (3, 1, 2), (3, 6, 3)),
        GuitarChord("G⁷", (1, 6, 1), (2, 2, 2), (3, 1, 3)),
        GuitarChord("Gm", (3, 1, 1), (3, 4, 1), (3, 5, 1), (3, 6, 1), (5, 2, 3), (5, 3, 4)),
    ]


if __name__ == "__main__":
    Guitar()()
