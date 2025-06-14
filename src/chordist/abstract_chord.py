from abc import ABC

from chordist.modifier import Modifier
from chordist.note import Note


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
