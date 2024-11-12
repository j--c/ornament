from ornament.helper import unpack_s
from ornament.helper import unpack_i
from ornament.helper import unpack_l
from ornament.helper import unpack_b
from ornament.helper import pack_s
from ornament.helper import pack_i
from ornament.helper import pack_l
from ornament.helper import pack_b
import unittest


class TestHelper(unittest.TestCase):

    def test_pack_unpack_s(self) -> None:

        # Given a string "the string"
        s = 'the string'

        # When I call pack_s on the string
        # and call unpack_s on the packed string
        packed_s = pack_s(s)
        unpacked_s = unpack_s(packed_s)

        # Then unpacked string equals the original string
        self.assertEqual(unpacked_s, 'the string')

    def test_pack_unpack_i(self) -> None:

        # Given an integer
        n = 73965

        # When I call pack_i on the integer
        # and call unpack_i on the packed integer
        packed_n = pack_i(n)
        unpacked_n = unpack_i(packed_n)

        # Then unpacked integer equals the original integer
        self.assertEqual(unpacked_n, 73965)

    def test_pack_unpack_i_too_big(self) -> None:

        # Given an integer that is more than 4 bytes
        n = 1073741826

        # When I call pack_i on the integer
        # Then it raises ValueError
        with self.assertRaises(ValueError):
            pack_i(n)

    def test_pack_unpack_l(self) -> None:

        # Given an long
        n = 1073741828

        # When I call pack_l on the long
        # and call unpack_l on the packed long
        packed_n = pack_l(n)
        unpacked_n = unpack_l(packed_n)

        # Then unpacked long equals the original long
        self.assertEqual(unpacked_n, 1073741828)

    def test_pack_unpack_l_too_big(self) -> None:

        # Given an long that is more than 8 bytes
        n = 9223372036854775808

        # When I call pack_l on the long
        # Then it raises ValueError
        with self.assertRaises(ValueError):
            pack_l(n)

    def test_pack_unpack_b(self) -> None:

        # Given a boolean
        b = False

        # When I call pack_b on the boolean
        # and call unpack_b on the packed boolean
        packed_b = pack_b(b)
        unpacked_b = unpack_b(packed_b)

        # Then unpacked boolean equals the original boolean
        self.assertFalse(unpacked_b)
