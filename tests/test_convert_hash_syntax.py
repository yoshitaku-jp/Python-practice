import unittest

from package.convert_hash_syntax import convert_hash_syntax

class TestConvertHashSyntax(unittest.TestCase):
    def test_convert_hash_syntax(self):
        self.assertEqual({}, convert_hash_syntax({}))
