import unittest

from package import gate


class TestGate(unittest.TestCase):
    def test_gate(self):

        umeda = gate.Gate(umeda)
        juso = gate.Gate(juso)
        ticket = ticket.Ticket(150)
        umeda.entry(ticket)
        self.assertTrue(juso.exit(ticket))
