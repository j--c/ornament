from ornament.table import PersonTable
from unittest.mock import patch
from io import BytesIO
import unittest


class TestPersonTable(unittest.TestCase):

    # @patch('ornament.storage.open_binary_file')
    def test_description(self) -> None:
        # Given a FileStorage
        #mock_open.return_value = self._bytes_io()
        pt = PersonTable('tmp.db')
        pt.add_row({
            'name': 'jc', 'address': 'washington',
            'telephone': '555.555.5555'
        })
        pt.close()

    # Private -----------------------------------------
    def _bytes_io(self) -> BytesIO:
        return BytesIO(b'123456789')

    def _dummy_path(self) -> str:
        return 'dummypath'
