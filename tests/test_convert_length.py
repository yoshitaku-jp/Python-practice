import unittest

from package.convert_length import convert_length


class TestConvertLengthTest(unittest.TestCase):
    def test_convert_length(self):
        self.assertEqual(39.37, convert_length(1, "m", "in"))
        self.assertEqual(0.38, convert_length(15, "in", "m"))
        self.assertEqual(10670.73, convert_length(35000, "ft", "m"))
