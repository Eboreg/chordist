import sys
from abc import ABC
from typing import Iterable

from chordist.chord import Chord
from chordist.constants import MAXLEN, XPAD, YPAD
from chordist.lyrics import split_lyrics_and_chords
from chordist.utils import filter_not_none


class AbstractInstrument(ABC):
    base_chords: list[Chord]
    string_count: int

    def __init__(self):
        self.min_chord_width = (self.string_count * 2) + 4

    def __call__(self):
        arg1 = sys.argv[1] if len(sys.argv) > 1 else None

        if arg1 == "--example":
            self.print_example()
        elif arg1 == "--example2":
            self.print_example2()
        else:
            self.print_chord_matrix()

    def find_chord(self, name: str, chords: Iterable[Chord] | None = None) -> Chord | None:
        return Chord.find(name, (chords or []) + self.base_chords)

    def print_chord_matrix(self, chords: Iterable[Chord] | None = None, **kwargs):
        Chord.print_matrix(chords or self.base_chords, min_chord_width=self.min_chord_width, **kwargs)

    def print_lyrics(
        self,
        lyrics: Iterable[Iterable[str] | str],
        title: str = "",
        chords: Iterable[Chord] | None = None,
        chords_on_top: bool = False,
        only_ascii: bool = False,
        maxlen: int = MAXLEN,
        xpad: int = XPAD,
        ypad: int = YPAD,
    ):
        rows, chord_names = split_lyrics_and_chords(
            lyrics,
            chords=(chords or []) + self.base_chords,
            only_ascii=only_ascii,
        )
        used_chords = filter_not_none(self.find_chord(c, chords) for c in chord_names)
        chord_matrix = "\n".join(
            Chord.generate_matrix(
                used_chords,
                maxlen=maxlen,
                xpad=xpad,
                ypad=ypad,
                min_chord_width=self.min_chord_width,
                only_ascii=only_ascii,
            )
        )

        if title:
            print(title)
            print("=" * len(title), end="\n\n")

        if used_chords and chords_on_top:
            print(chord_matrix)
            print()

        for row in rows:
            print(row)

        if used_chords and not chords_on_top:
            print()
            print(chord_matrix)

    def print_example(self):
        verses = [
            [
                "[G]Ain't gonna work on the railroad",
                "Ain't gonna work on the [D7]farm",
                "Gonna [G]lay around the shack",
                "'Til the [C]mail train comes back",
                "And [D7]roll in my sweet baby's [G]arms",
            ],
            [
                "Now [G]where was you last Friday night",
                "While I was lyin' in [D7]jail?",
                "[G]Walkin' the streets with a[C]nother man",
                "[D7]Wouldn't even go my [G]bail",
            ],
        ]
        chorus = [
            "[G]Roll in my sweet baby's arms",
            "Roll in my sweet baby's [D7]arms",
            "Gonna [G]lay around the shack",
            "'Til the [C]mail train comes back",
            "And [D7]roll in my sweet baby's [G]arms",
        ]
        song = [chorus, verses[0], chorus, verses[1], chorus]
        self.print_lyrics(song, title="Roll in My Sweet Baby's Arms")

    def print_example2(self):
        chorus = [
            "[G]Roll in my sweet baby's arms",
            "Roll in my sweet baby's [D⁷]arms",
            "Gonna [G]lay around the shack",
            "'Til the [C]mail train comes back",
            "And [D⁷]roll in my sweet baby's [G]arms",
        ]
        self.print_lyrics(chorus, title="Roll in My Sweet Baby's Arms", only_ascii=True)
