import unittest

from package.rgb import to_hex, to_ints


class TestRgb(unittest.TestCase):
    def test_to_hex(self):
        self.assertEqual("#000000", to_hex(0, 0, 0))
        self.assertEqual("#ffffff", to_hex(255, 255, 255))
        self.assertEqual("#043c78", to_hex(4, 60, 120))

    def test_to_ints(self):
        self.assertEqual([0, 0, 0], to_ints("#000000"))
        self.assertEqual([255, 255, 255], to_ints("#ffffff"))
        self.assertEqual([4, 60, 120], to_ints("#043c78"))
