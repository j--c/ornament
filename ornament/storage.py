from ornament.helper import open_binary_file
from io import BufferedIOBase
from os import SEEK_CUR


# TODO - this should inherit from base class
class FileStorage(object):

    _handle: BufferedIOBase

    # initializes and opens a binary file stream
    def __init__(self, path: str) -> None:
        self._handle = open_binary_file(path, 'r+b')

    # closes the binary file stream
    def close(self) -> None:
        self._handle.close()

    # read bytes of specified len (dlen) from the position and whence specified
    def read(self, dlen: int, pos: int = 0, whence: int = SEEK_CUR) -> bytes:
        self._handle.seek(pos, whence)
        return self._handle.read(dlen)

    # write bytes of data to the position and whence specified
    def write(self, data: bytes, pos: int = 0, whence: int = SEEK_CUR) -> int:
        self._handle.seek(pos, whence)
        return self._handle.write(data)

    # return the current position of the cursor in the binary stream
    def cur_pos(self) -> int:
        return self._handle.tell()
