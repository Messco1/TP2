import unittest
from tp2 import fizzBuzz

class testFizzBuzz (unittest.TestCase):

    def setUp(self) -> None:
        self.instance = fizzBuzz("MonObjet")