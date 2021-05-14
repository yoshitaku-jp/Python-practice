import unittest

from lib.rgb import to_hex


class TestRgb(unittest.TestCase):
    def test_to_hex(self):
        self.assertEqual("#000000", to_hex(0, 0, 0))
