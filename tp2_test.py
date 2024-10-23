import unittest
from tp2 import fizzBuzz

class testFizzBuzz (unittest.TestCase):

    def setUp(self) -> None:
        self.instance = fizzBuzz("MonObjet")


    def test_fizzBuzz(self):
        self.assertEqual(self.instance.affiche(5, 10), "BuzzFizz78FizzBuzz")
        self.assertEqual(self.instance.affiche(10, 16), "Buzz11Fizz1314FrisBee16")

if __name__=="__main__":
    unittest.main()

