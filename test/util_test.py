import unittest
from util import operand, NotEnoughNumbers, InvalidOperand


class UtilTest(unittest.TestCase):
    def setUp(self):
        self.pile = [10, 5, 6]


    def test_zero_division(self):
        self.pile.append(0)
        self.assertRaises(ZeroDivisionError, operand, self.pile, "/")

    def test_invalid_operation(self):
        self.assertRaises(InvalidOperand, operand, self.pile, "tdq")

    def test_not_enough_elements(self):
        p = []
        self.assertRaises(NotEnoughNumbers, operand, p, "/")

    def test_operand_addition(self):
        self.assertEqual(operand(self.pile, "+"), 11)

    def test_operand_soustraction(self):
        self.assertEqual(operand(self.pile, "-"), -1)

    def test_operand_multiplication(self):
        self.assertEqual(operand(self.pile, "*"), 30)

    def test_operand_division(self):
        self.assertEqual(operand(self.pile, "/"), 0.8333333333333334)
