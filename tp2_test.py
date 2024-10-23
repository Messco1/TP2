import unittest
from tp2 import fizzBuzz

class testFizzBuzz (unittest.TestCase):

    def setUp(self) -> None:
        self.instance = fizzBuzz("MonObjet")


    def test_fizzBuzz(self):
        self.assertEqual(self.instance.affiche(15), "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee")


if __name__=="__main__":
    unittest.main()

