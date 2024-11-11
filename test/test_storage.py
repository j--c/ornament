import unittest
from ornament.storage import FileStorage
from unittest.mock import patch
from io import BytesIO
from os import SEEK_SET
from os import SEEK_END


# TODO - whole read / write mechanism needs to be mocked
class TestFileStorage(unittest.TestCase):

    def test_construct_w_invalid_path(self):
        with self.assertRaises(FileNotFoundError):
            FileStorage(self._dummy_path())

    @patch('ornament.storage.open_binary_file')
    def test_read_write_s_begin_file(self, mock_open):
        mock_open.return_value = BytesIO(b'123456789')
        fs = FileStorage(self._dummy_path())
        s_to_write = 'begin'
        fs.write_s(s_to_write, 0, SEEK_SET)
        s_read = fs.read_s(5, 0, SEEK_SET)
        fs.close()
        self.assertEqual(s_read, s_to_write)

    @patch('ornament.storage.open_binary_file')
    def test_read_write_s_end_file(self, mock_open):
        mock_open.return_value = BytesIO(b'123456789')
        fs = FileStorage(self._dummy_path())
        s_to_write = 'end'
        fs.write_s(s_to_write, 0, SEEK_END)
        s_read = fs.read_s(3, -3, SEEK_END)
        fs.close()
        self.assertEqual(s_read, s_to_write)

    @patch('ornament.storage.open_binary_file')
    def test_read_write_i_begin_file(self, mock_open):
        mock_open.return_value = BytesIO(b'123456789')
        fs = FileStorage(self._dummy_path())
        fs.write_i(89, 0, SEEK_SET)
        i_read = fs.read_i(0, SEEK_SET)
        fs.close()
        self.assertEqual(i_read, 89)

    @patch('ornament.storage.open_binary_file')
    def test_read_write_i_end_file(self, mock_open):
        mock_open.return_value = BytesIO(b'123456789')
        fs = FileStorage(self._dummy_path())
        fs.write_i(29789, 0, SEEK_END)
        i_read = fs.read_i(-4, SEEK_END)
        fs.close()
        self.assertEqual(i_read, 29789)

    @patch('ornament.storage.open_binary_file')
    def test_read_write_b_begin_file(self, mock_open):
        mock_open.return_value = BytesIO(b'123456789')
        fs = FileStorage(self._dummy_path())
        fs.write_b(False, 0, SEEK_SET)
        b_read = fs.read_b(0, SEEK_SET)
        fs.close()
        self.assertEqual(b_read, False)

    @patch('ornament.storage.open_binary_file')
    def test_read_write_b_end_file(self, mock_open):
        mock_open.return_value = BytesIO(b'123456789')
        fs = FileStorage(self._dummy_path())
        fs.write_b(False, 0, SEEK_END)
        b_read = fs.read_b(-1, SEEK_END)
        fs.close()
        self.assertEqual(b_read, False)

    def _dummy_path(self) -> str:
        return 'dummypath'
