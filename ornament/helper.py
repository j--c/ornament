from io import BufferedIOBase
from os.path import exists
import struct

STR_ENCODING = 'utf-8'
LNG_MAX = 9223372036854775807
INT_MAX = 1073741824


def open_binary_file(path: str, mode: str) -> BufferedIOBase:
    if exists(path):
        return open(path, mode)
    else:
        not_found_msg = f'File not found at: {path}!'
        raise FileNotFoundError(not_found_msg)


# Strings -----------------------------------------
def pack_s(s: str, encoding: str = None) -> bytes:
    if encoding is None:
        encoding = STR_ENCODING
    s_encoded = s.encode(encoding)
    s_len = len(s_encoded)
    pack_format = f'@{s_len}s'
    return struct.pack(pack_format, s_encoded)


def unpack_s(data: bytes, encoding: str = None) -> str:
    if encoding is None:
        encoding = STR_ENCODING
    pack_format = f'@{len(data)}s'
    s_encoded = struct.unpack(pack_format, data)[0]
    return s_encoded.decode(encoding)


# Whole Numbers ----------------------------------
def pack_n(n: int) -> bytes:

    if n < INT_MAX:
        return pack_i(n)
    else:
        return pack_l(n)


# Integers ----------------------------------------
def pack_i(n: int) -> bytes:
    pack_format = '@i'
    if n < INT_MAX:
        return struct.pack(pack_format, n)
    else:
        val_msg = f'pack_i requires value less than or equal to {INT_MAX}'
        raise ValueError(val_msg)


def unpack_i(data: bytes) -> int:
    pack_format = '@i'
    return struct.unpack(pack_format, data)[0]


# Longs -------------------------------------------
def pack_l(n: int) -> bytes:
    pack_format = '@l'
    if n < LNG_MAX:
        return struct.pack(pack_format, n)
    else:
        val_msg = f'pack_l requires value less than or equal to {LNG_MAX}'
        raise ValueError(val_msg)


def unpack_l(data: bytes) -> int:
    pack_format = '@l'
    return struct.unpack(pack_format, data)[0]


# Booleans-----------------------------------------
def pack_b(b: bool) -> bytes:
    pack_format = '@?'
    return struct.pack(pack_format, b)


def unpack_b(data: bytes) -> bool:
    pack_format = '@?'
    return struct.unpack(pack_format, data)[0]
