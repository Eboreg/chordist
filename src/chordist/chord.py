import functools
import operator
from typing import Generator, Iterable

from chordist.constants import MAXLEN, XPAD, YPAD
from chordist.utils import split_before


def ascii_chord_name(name: str):
    return (
        name
        .replace("♭", "b")
        .replace("♯", "#")
        .replace("¹", "1")
        .replace("³", "3")
        .replace("⁵", "5")
        .replace("⁷", "7")
        .replace("⁹", "9")
    )


class Chord:
    string_count: int
    finger_map: dict[tuple[int, int], int | str]
    name: str
    ascii_name: str
    fret_rows: list[str]
    start_fret: int
    end_fret: int

    @property
    def height(self):
        return len(self.fret_rows) + 1

    @property
    def width(self):
        return max((len(row) for row in self.fret_rows))

    def __init__(self, name: str, string_count: int, *fingers: tuple[int, int, int | str] | tuple[int, int]):
        # fingers: [(fret, string, finger), (fret, string), ...]
        # (without finger, "*" will be printed)
        # fret & string = 1-indexed
        self.name = name
        self.string_count = string_count
        self.ascii_name = ascii_chord_name(name)
        self.finger_map = {(f[0], f[1]): f[2] if len(f) > 2 else "*" for f in fingers}
        highest_fret = max((f[0] for f in fingers), default=1)
        lowest_fret = min((f[0] for f in fingers), default=1)
        if highest_fret > 4:
            self.start_fret = lowest_fret
        else:
            self.start_fret = 1
        self.end_fret = max(self.start_fret + 3, highest_fret)
        self.fret_rows = []
        for fret in range(self.start_fret, self.end_fret + 1):
            self.fret_rows.append(self.generate_fret(fret))

    def __eq__(self, value):
        return (
            isinstance(value, Chord) and
            value.string_count == self.string_count and
            value.finger_map == self.finger_map and
            value.ascii_name == self.ascii_name
        )

    def generate_head(self, only_ascii: bool = False) -> str:
        name = self.ascii_name if only_ascii else self.name
        width = (self.string_count * 2) - 1
        fill = "_" if self.start_fret == 1 else " "
        head = fill * max(int((width / 2) - (len(name) / 2)), 0)
        head += name
        head += fill * max(width - len(head), 0)
        return head

    def generate_fret(self, fret: int) -> str:
        fret_str = ""

        for string in range(1, self.string_count + 1):
            if (fret, string) in self.finger_map:
                fret_str += str(self.finger_map[(fret, string)])
            else:
                fret_str += "|"
            if string < self.string_count:
                fret_str += " "

        if fret == self.start_fret and fret > 1:
            fret_str += f" {fret}fr"

        return fret_str

    def get_row(self, idx: int, pad: int = 0, min_width: int | None = None, only_ascii: bool = False) -> str:
        width = max(min_width, self.width) if min_width else self.width
        if idx - 1 >= len(self.fret_rows):
            return " " * (width + pad)
        if idx == 0:
            row = self.generate_head(only_ascii=only_ascii)
        else:
            row = self.fret_rows[idx - 1]
        return f"{row:{width + pad}s}"

    def get_width(self, pad: int = 0, min_width: int | None = None) -> int:
        width = self.width + pad
        if min_width and min_width > width:
            return min_width
        return width

    @staticmethod
    def find(names: Iterable[str], chords: Iterable["Chord"]) -> "list[Chord]":
        matches = []
        for name in names:
            for chord in chords:
                if name in (chord.name, chord.ascii_name) and chord not in matches:
                    matches.append(chord)
        return matches

    @staticmethod
    def generate_matrix(
        chords: Iterable["Chord"],
        maxlen: int = MAXLEN,
        xpad: int = XPAD,
        ypad: int = YPAD,
        min_chord_width: int | None = None,
        only_ascii: bool = False,
    ) -> "Generator[str]":
        def test_row_length(l: list[Chord]):
            return sum(c.get_width(pad=xpad, min_width=min_chord_width) for c in l) > maxlen

        rows = list(split_before(chords, test_row_length))

        for idx, row in enumerate(rows):
            if idx > 0 and ypad:
                yield "\n" * (ypad - 1)
            for y in range(max((c.height for c in row), default=0)):
                yield functools.reduce(
                    operator.add,
                    [c.get_row(y, pad=xpad, min_width=min_chord_width, only_ascii=only_ascii) for c in row],
                )

    @staticmethod
    def print_matrix(
        chords: Iterable["Chord"],
        maxlen: int = MAXLEN,
        xpad: int = XPAD,
        ypad: int = YPAD,
        min_chord_width: int | None = None,
        only_ascii: bool = False,
    ):
        for row in Chord.generate_matrix(
            chords,
            maxlen=maxlen,
            xpad=xpad,
            ypad=ypad,
            min_chord_width=min_chord_width,
            only_ascii=only_ascii,
        ):
            print(row)
