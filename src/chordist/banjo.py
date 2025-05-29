from chordist.abstract_instrument import AbstractInstrument
from chordist.chord import Chord


class BanjoChord(Chord):
    def __init__(self, name: str, *fingers: tuple[int, int, int | str] | tuple[int, int]):
        super().__init__(name, 4, *fingers)


class Banjo(AbstractInstrument):
    string_count = 4
    chords = [
        BanjoChord("A", (2, 1, 1), (2, 2, 1), (2, 3, 1), (2, 4, 1)),
        BanjoChord("A⁷", (2, 1, 1), (2, 2, 1), (2, 3, 1), (2, 4, 1)),
        BanjoChord("Am", (1, 3, 1), (2, 1, 2), (2, 2, 3), (2, 4, 4)),
        BanjoChord("A♭", (1, 1, 1), (1, 2, 1), (1, 3, 1), (1, 4, 1)),
        BanjoChord("A♭⁷", (4, 3, 1), (4, 4, 1), (5, 2, 2), (6, 1, 3)),
        BanjoChord("A♭m", (1, 1, 1), (1, 2, 2), (1, 4, 3)),
        BanjoChord("B", (4, 1, 1), (4, 2, 1), (4, 3, 1), (4, 4, 1)),
        BanjoChord("B⁷", (1, 1, 1), (1, 4, 2), (2, 2, 3)),
        BanjoChord("Bm", (3, 3, 1), (4, 1, 2), (4, 2, 3)),
        BanjoChord("B♭", (3, 2, 1), (3, 3, 1), (3, 4, 1)),
        BanjoChord("B♭⁷", (6, 3, 1), (6, 4, 1), (7, 2, 2), (8, 1, 3)),
        BanjoChord("B♭m", (6, 2, 1), (6, 3, 1), (8, 1, 3), (8, 4, 4)),
        BanjoChord("C", (1, 3, 1), (2, 1, 2), (2, 4, 3)),
        BanjoChord("C⁷", (8, 3, 1), (8, 4, 1), (9, 2, 2), (10, 1, 3)),
        BanjoChord("Cm", (1, 1, 1), (1, 3, 2), (1, 4, 3)),
        BanjoChord("C♯", (9, 3, 1), (10, 2, 2), (11, 1, 3), (11, 4, 4)),
        BanjoChord("C♯⁷", (9, 3, 1), (9, 4, 1), (10, 2, 2), (11, 1, 3)),
        BanjoChord("C♯m", (9, 2, 1), (9, 3, 1), (11, 1, 3), (11, 4, 4)),
        BanjoChord("D", (2, 2, 1), (3, 3, 2), (4, 4, 3)),
        BanjoChord("D⁷", (1, 3, 1), (2, 2, 2), (4, 4, 4)),
        BanjoChord("Dm", (2, 2, 1), (3, 3, 2), (3, 4, 3)),
        BanjoChord("E", (1, 2, 1), (2, 1, 2), (2, 4, 3)),
        BanjoChord("E⁷", (1, 2, 1), (2, 1, 2)),
        BanjoChord("Em", (2, 1, 2), (2, 4, 3)),
        BanjoChord("E♭", (3, 2, 1), (4, 3, 2), (5, 1, 3), (5, 4, 4)),
        BanjoChord("E♭⁷", (1, 1, 1), (2, 3, 2), (3, 2, 3), (5, 4, 4)),
        BanjoChord("E♭m", (3, 2, 1), (4, 1, 2), (4, 3, 3), (4, 4, 4)),
        BanjoChord("F", (1, 3, 1), (2, 2, 2), (3, 1, 3), (3, 4, 4)),
        BanjoChord("F⁷", (1, 3, 1), (1, 4, 1), (2, 2, 2), (3, 1, 3)),
        BanjoChord("Fm", (1, 2, 1), (1, 3, 1), (3, 1, 3), (3, 4, 4)),
        BanjoChord("F♯", (2, 3, 1), (3, 2, 2), (4, 1, 3), (4, 4, 4)),
        BanjoChord("F♯⁷", (2, 3, 1), (2, 4, 1), (3, 2, 2), (4, 1, 3)),
        BanjoChord("F♯m", (2, 2, 1), (2, 3, 1), (4, 1, 3), (4, 4, 4)),
        BanjoChord("G"),
        BanjoChord("G⁷", (3, 4, 3)),
        BanjoChord("Gm", (3, 2, 1), (3, 3, 2)),
    ]


if __name__ == "__main__":
    Banjo()()
