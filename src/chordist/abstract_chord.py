from abc import ABC, abstractmethod
from typing import Iterable, Self, TypeVar

from chordist.note import Note


_ChordT = TypeVar("_ChordT", bound="AbstractChord")


class Modifier:
    # pylint: disable=redefined-builtin
    def __init__(self, name: str, ascii: str = "", alt_names: list[str] | None = None):
        self.name = name
        self.ascii = ascii or name
        self.alt_names = alt_names or []

    def __eq__(self, value: object) -> bool:
        if isinstance(value, str):
            name = value
        elif isinstance(value, Modifier):
            name = value.name
        else:
            return False
        return name in [self.name, self.ascii, *self.alt_names]

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self):
        names = set([self.name, self.ascii, *self.alt_names])
        return f"Modifier({names})"


class Modifiers:
    class NotFound(Exception):
        ...

    AUG = Modifier("+", alt_names=["aug"])
    DIM7 = Modifier("dim⁷", "dim7")
    MAJ7 = Modifier("maj⁷", "maj7")
    MINOR = Modifier("m")
    MINOR7 = Modifier("m⁷", "m7")
    SEVEN = Modifier("⁷", "7")
    SUS2 = Modifier("sus2")
    SUS4 = Modifier("sus4")

    @classmethod
    def get(cls, name: str) -> Modifier:
        for value in cls.__dict__.values():
            if isinstance(value, Modifier) and value == name:
                return value
        raise Modifiers.NotFound(f"Modifier {name} not found")


class AbstractChord(ABC):
    base: Note
    modifier: Modifier | None

    def __eq__(self, value: object) -> bool:
        if isinstance(value, str):
            for idx in range(len(value), 0, -1):
                if self.base == value[:idx]:
                    if idx < len(value):
                        if self.modifier == value[idx:]:
                            return True
                    elif self.modifier is None:
                        return True
            return False
        return isinstance(value, AbstractChord) and value.base == self.base and value.modifier == self.modifier


class AbstractChordCollection(Iterable[_ChordT]):
    chords: list[_ChordT]

    def __init__(self, *chords: _ChordT):
        unique_chords: list[_ChordT] = []
        for chord in chords:
            if chord not in unique_chords:
                unique_chords.append(chord)
        self.chords = unique_chords

    @abstractmethod
    def __add__(self, other: "AbstractChordCollection[_ChordT]") -> Self:
        ...

    def __iter__(self):
        return iter(self.chords)

    def __repr__(self):
        return repr(self.chords)

    def add(self, chord: _ChordT) -> Self:
        if chord not in self.chords:
            self.chords.append(chord)
        return self

    @abstractmethod
    def filter(self, name: str) -> Self:
        ...

    def first(self) -> _ChordT | None:
        if self.chords:
            return self.chords[0]
        return None

    def update(self, chords: Iterable[_ChordT]) -> Self:
        for chord in chords:
            if chord not in self.chords:
                self.chords.append(chord)
        return self
