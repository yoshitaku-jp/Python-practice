import unittest

from package.convert_length import convert_length


class TestConvertLengthTest(unittest.TestCase):
    def test_convert_length(self):
        self.assertEqual(39.37, convert_length(1, "m", "in"))
