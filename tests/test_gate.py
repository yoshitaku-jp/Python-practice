import unittest

from package import gate


class TestGate(unittest.TestCase):
    def test_gate(self):
        self.assertTrue(gate.Gate())
