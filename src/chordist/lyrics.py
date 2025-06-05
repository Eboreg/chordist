import dataclasses
import re
from typing import Generator, Iterable

from chordist.chord import Chord


@dataclasses.dataclass
class LyricsRowPiece:
    lyric: str
    chord_name: str
    chord: Chord | None = None

    def get_chord_name(self, only_ascii: bool = False) -> str:
        if self.chord:
            return self.chord.ascii if only_ascii else self.chord.name
        return self.chord_name

    def get_lyric(self, only_ascii: bool = False) -> str:
        chord_name = self.get_chord_name(only_ascii)
        lyric = self.lyric
        if len(lyric) <= len(chord_name):
            lyric += "-"
            lyric = f"{lyric:{len(chord_name) + 1}s}"
        return lyric

    def transpose(self, steps: int):
        if self.chord_name and self.chord is None:
            raise ValueError(f"Could not transpose lyric '{self.lyric}': unidentified chord '{self.chord_name}'")
        return LyricsRowPiece(
            lyric=self.lyric,
            chord_name=self.chord_name,
            chord=self.chord.transpose(steps) if self.chord else None,
        )


@dataclasses.dataclass
class LyricsRow:
    pieces: list[LyricsRowPiece] = dataclasses.field(default_factory=list)
    used_chords: list[Chord] = dataclasses.field(default_factory=list, init=False)

    def __post_init__(self):
        for piece in self.pieces:
            if piece.chord and piece.chord not in self.used_chords:
                self.used_chords.append(piece.chord)

    @classmethod
    def create(cls, row: str):
        patt = r"(?:\[(.*?)\])?([^[]*)"
        pieces: list[LyricsRowPiece] = []

        for chord_name, lyric in re.findall(patt, row):
            if chord_name or lyric:
                if chord_name:
                    chord = Chord.get_or_null(chord_name)
                else:
                    chord = None
                pieces.append(LyricsRowPiece(lyric, chord_name, chord))

        return LyricsRow(pieces=pieces)

    def get_chords_row(self, only_ascii: bool = False):
        if not self.pieces:
            return None
        result = ""
        for piece in self.pieces:
            result += f"{piece.get_chord_name(only_ascii):{len(piece.get_lyric(only_ascii))}s}"
        return result.rstrip()

    def get_lyrics_row(self, only_ascii: bool = False):
        result = ""
        for piece in self.pieces:
            result += piece.get_lyric(only_ascii)
        return result.rstrip(" -")

    def print(self, only_ascii: bool = False):
        chords_row = self.get_chords_row(only_ascii)
        lyrics_row = self.get_lyrics_row(only_ascii)
        if chords_row is not None:
            print(chords_row)
        print(lyrics_row)

    def transpose(self, steps: int):
        return LyricsRow([p.transpose(steps) for p in self.pieces])


@dataclasses.dataclass
class Lyrics:
    rows: list[LyricsRow] = dataclasses.field(default_factory=list)
    used_chords: list[Chord] = dataclasses.field(default_factory=list, init=False)

    def __post_init__(self):
        for row in self.rows:
            for chord in row.used_chords:
                if chord not in self.used_chords:
                    self.used_chords.append(chord)

    @classmethod
    def create(cls, lyrics: Iterable[Iterable[str] | str]):
        rows: list[LyricsRow] = []

        for row in cls.normalize_lyrics(lyrics):
            rows.append(LyricsRow.create(row))

        return Lyrics(rows=rows)

    @classmethod
    def normalize_lyrics(cls, lyrics: Iterable[Iterable[str] | str]) -> "Generator[str]":
        """Inserts blank row between verses"""
        for idx, row in enumerate(lyrics):
            if isinstance(row, str):
                yield row
            else:
                if idx > 0:
                    yield ""
                yield from row

    def print(self, only_ascii: bool = False):
        for row in self.rows:
            row.print(only_ascii=only_ascii)

    def transpose(self, steps: int):
        return Lyrics([r.transpose(steps) for r in self.rows])
