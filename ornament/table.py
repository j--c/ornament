from ornament.storage import FileStorage
from os import SEEK_END


# implemented as a singleton
class TableIndex(object):

    _index: dict[int, int]
    _row_count: int

    def __new__(cls) -> None:
        if not hasattr(cls, 'instance'):
            cls.instance = super(TableIndex, cls).__new__(cls)
            cls.instance._index = {}
            cls.instance._row_count = 0
        return cls.instance

    def __init__(self):
        pass

    def add_row(self, pos: int) -> None:
        self._index[self._row_count] = pos
        self._row_count += 1

    def remove_row(self, row_num: int) -> None:
        self._index.pop(row_num)
        self._row_count -= 1

    def row_count(self) -> int:
        return self._row_count


# TODO - this should inherit from base class
class PersonTable(object):

    _storage: FileStorage
    _index: TableIndex

    def __init__(self, storage_path: str) -> None:
        self._storage = FileStorage(storage_path)
        self._index = TableIndex()

    def add_row(self, person: dict) -> None:
        row_length = (
            len(person['name']) + len(person['address']),
            len(person['telephone'])
        )
        self._storage.write_i(row_length, 0, SEEK_END)
        self._storage.write_s(person['name'], 0, SEEK_END)

    def close(self) -> None:
        self._storage.close()
