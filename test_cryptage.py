import unittest
from cryptage import crypt

class TestCryptage(unittest.TestCase):
    def test_crypt(self):
        self.assertEqual(crypt("abc"), "bcd")

if __name__ == "__main__":
    unittest.main()