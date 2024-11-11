from io import BufferedIOBase
from os.path import exists


def open_binary_file(path: str, mode: str) -> BufferedIOBase:
    if exists(path):
        return open(path, mode)
    else:
        not_found_msg = f'File not found at: {path}!'
        raise FileNotFoundError(not_found_msg)
