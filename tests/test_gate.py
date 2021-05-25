import unittest

from package import gate, ticket


class TestGate(unittest.TestCase):
    def test_gate(self):

        umeda = gate.Gate("umeda")
        juso = gate.Gate("juso")
        ticket1 = ticket.Ticket(150)
        umeda.enter(ticket1)
        self.assertTrue(juso.exit(ticket1))

    def test_umeda_to_mikuni_when_fare_is_not_enough(self):
        umeda = gate.Gate("umeda")
        mikuni = gate.Gate("juso")

        ticket1 = ticket.Ticket(150)
        umeda.enter(ticket1)
        self.assertFalse(mikuni.exit(ticket1))
