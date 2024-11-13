from ornament.storage import FileStorage
from ornament.helper import pack_s
from ornament.helper import pack_n
from ornament.helper import pack_b
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

    def add_row(self, row: dict) -> None:
        packed_row = self._pack_row(row)
        self._write_row(packed_row)

    def close(self) -> None:
        self._storage.close()

    def _pack_row(self, row: dict) -> dict:
        row_len = 0
        packed_row = {}
        for k, v in row.items():
            packed_row[k] = self._get_packed_value(v)
            packed_row[f'{k}_len'] = self._get_packed_value(len(packed_row[k]))
            row_len += len(packed_row[k])
            row_len += len(packed_row[f'{k}_len'])

        packed_row['deleted'] = self._get_packed_value(False)
        packed_row['row_len'] = self._get_packed_value(row_len)
        return packed_row

    def _write_row(self, packed_row: dict) -> None:
        self._storage.write(packed_row['deleted'], 0, SEEK_END)
        self._storage.write(packed_row['row_len'], 0, SEEK_END)

        self._storage.write(packed_row['name_len'], 0, SEEK_END)
        self._storage.write(packed_row['name'], 0, SEEK_END)

        self._storage.write(packed_row['address_len'], 0, SEEK_END)
        self._storage.write(packed_row['address'], 0, SEEK_END)

        self._storage.write(packed_row['telephone_len'], 0, SEEK_END)
        self._storage.write(packed_row['telephone'], 0, SEEK_END)

    def _get_packed_value(self, val) -> bytes:
        val_type = type(val)
        return_bytes = None
        if val_type == int:
            return_bytes = pack_n(val)
        elif val_type == str:
            return_bytes = pack_s(val)
        elif val_type == bool:
            return_bytes = pack_b(val)
        return return_bytes
