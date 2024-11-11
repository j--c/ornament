from ornament.helper import open_binary_file
from io import BufferedIOBase
from os import SEEK_CUR
import struct

STR_ENCODING = 'utf-8'
LNG_MAX = 9223372036854775807
INT_MAX = 1073741824


# TODO - this should inherit from base class
class FileStorage(object):

    _handle: BufferedIOBase

    def __init__(self, path: str) -> None:
        self._handle = open_binary_file(path, 'r+b')

    def close(self) -> None:
        self._handle.close()

    def read(self, dlen: int, pos: int = 0, whence: int = SEEK_CUR) -> bytes:
        self._handle.seek(pos, whence)
        return self._handle.read(dlen)

    def write(self, data: bytes, pos: int = 0, whence: int = SEEK_CUR) -> int:
        self._handle.seek(pos, whence)
        return self._handle.write(data)

    # Strings -----------------------------------------
    def read_s(self, dlen: int, pos: int = 0, whence: int = SEEK_CUR) -> str:
        pack_format = f'@{dlen}s'
        data = self.read(dlen, pos, whence)
        s_encoded = struct.unpack(pack_format, data)[0]
        return s_encoded.decode(STR_ENCODING)

    def write_s(self, s: str, pos: int = 0, whence: int = SEEK_CUR) -> int:
        s_encoded = s.encode(STR_ENCODING)
        s_len = len(s_encoded)
        pack_format = f'@{s_len}s'
        return self.write(struct.pack(pack_format, s_encoded), pos, whence)

    # Integers ----------------------------------------
    def read_i(self, pos: int = 0, whence: int = SEEK_CUR) -> int:
        pack_format = '@i'
        data = self.read(4, pos, whence)
        return struct.unpack(pack_format, data)[0]

    def write_i(self, n: int, pos: int = 0, whence: int = SEEK_CUR) -> int:
        pack_format = '@i'
        if n > INT_MAX:
            val_msg = f'write_l requires value less than or equal to {LNG_MAX}'
            raise ValueError(val_msg)
        return self.write(struct.pack(pack_format, n), pos, whence)

    # Longs -------------------------------------------
    def read_l(self, pos: int = 0, whence: int = SEEK_CUR) -> int:
        pack_format = '@l'
        data = self.read(8, pos, whence)
        return struct.unpack(pack_format, data)[0]

    def write_l(self, n: int, pos: int = 0, whence: int = SEEK_CUR) -> int:
        pack_format = '@l'
        if n > LNG_MAX:
            return self.write(struct.pack(pack_format, n), pos, whence)
        else:
            val_msg = f'write_l requires value less than or equal to {LNG_MAX}'
            raise ValueError(val_msg)

    # Booleans-----------------------------------------
    def read_b(self, pos: int = 0, whence: int = SEEK_CUR) -> bool:
        pack_format = '@?'
        data = self.read(1, pos, whence)
        return struct.unpack(pack_format, data)[0]

    def write_b(self, b: bool, pos: int = 0, whence: int = SEEK_CUR) -> int:
        pack_format = '@?'
        return self.write(struct.pack(pack_format, b), pos, whence)
