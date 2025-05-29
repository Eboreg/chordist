import re
from typing import Generator, Iterable

from chordist.chord import Chord


def normalize_lyrics(lyrics: Iterable[Iterable[str] | str]) -> "Generator[str]":
    """Inserts blank row between verses"""
    for idx, row in enumerate(lyrics):
        if isinstance(row, str):
            yield row
        else:
            if idx > 0:
                yield ""
            yield from row


def split_lyrics_and_chords(
    lyrics: Iterable[Iterable[str] | str],
    chords: Iterable[Chord] | None = None,
    only_ascii: bool = False,
) -> tuple[list[str], list[str]]:
    patt = r"\[(.*?)\]"
    chords = chords or []
    chord_names = []
    rows = []

    for row in normalize_lyrics(lyrics):
        parts = re.split(patt, row)
        lyrics_row = ""
        chords_row = ""
        for idx, part in enumerate(parts):
            if not idx % 2:
                lyrics_row += part
            else:
                chord = Chord.find(part, chords)
                chord_name = part
                if chord:
                    chord_name = chord.ascii_name if only_ascii else chord.name
                if chord_name not in chord_names:
                    chord_names.append(chord_name)
                chords_row = f"{chords_row:{len(lyrics_row)}s}{chord_name}"
        if chords_row:
            rows.append(chords_row)
        rows.append(lyrics_row)

    return rows, chord_names
