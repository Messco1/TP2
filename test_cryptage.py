import unittest
from cryptage import crypt

class TestCryptage(unittest.TestCase):
    def test_crypt(self):
        self.assertEqual(crypt("abc", 1), "bcd 1")

if __name__ == "__main__":
    unittest.main()