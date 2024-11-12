import unittest
from ornament.storage import FileStorage
from unittest.mock import patch
from io import BytesIO
from os import SEEK_SET
from os import SEEK_END


# TODO - whole read / write mechanism needs to be mocked
class TestFileStorage(unittest.TestCase):

    def test_construct_w_invalid_path(self) -> None:
        with self.assertRaises(FileNotFoundError):
            FileStorage(self._dummy_path())

    @patch('ornament.storage.open_binary_file')
    def test_read_write_end_file(self, mock_open) -> None:

        # Given a FileStorage
        mock_open.return_value = self._bytes_io()
        fs = self._file_storage()

        # When I write to the end of the FileStoraga and
        # read from the end of the FileStorage
        fs.write(bytes('str', 'utf-8'), 0, SEEK_END)
        d_from_fs = fs.read(3, -3, SEEK_END)
        fs.close()

        # Then the value read is equal to the value written
        self.assertEqual(bytes('str', 'utf-8'), d_from_fs)

    @patch('ornament.storage.open_binary_file')
    def test_read_write_begin_file(self, mock_open) -> None:

        # Given a FileStorage
        mock_open.return_value = self._bytes_io()
        fs = self._file_storage()

        # When I write to the beginning of the FileStorage and
        # read from the beginning of the FileStorage
        fs.write(bytes('string', 'utf-8'), 0, SEEK_SET)
        d_from_fs = fs.read(6, 0, SEEK_SET)
        fs.close()

        # Then the value read is equal to the value written
        self.assertEqual(bytes('string', 'utf-8'), d_from_fs)

    @patch('ornament.storage.open_binary_file')
    def test_current_pos(self, mock_open) -> None:

        # Given a FileStorage
        mock_open.return_value = self._bytes_io()
        fs = self._file_storage()

        # When I move to the 6th position by writing
        # a 6 char string
        fs.write(bytes('string', 'utf-8'), 0, SEEK_SET)
        cur_pos = fs.cur_pos()
        fs.close()

        # Then the value returned by FileStorage.cur_pos() is 6
        self.assertEqual(cur_pos, 6)

    # Private -----------------------------------------
    def _bytes_io(self) -> BytesIO:
        return BytesIO(b'123456789')

    def _file_storage(self) -> FileStorage:
        return FileStorage(self._dummy_path)

    def _dummy_path(self) -> str:
        return 'dummypath'
