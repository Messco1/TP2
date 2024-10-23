import unittest
from cryptage import crypt
from cryptage import decrypt


class TestCryptage(unittest.TestCase):
    def test_decrypt(self):
        encrypted = crypt("abc", 1)
        self.assertEqual(decrypt(encrypted), "abc")

if __name__ == "__main__":
    unittest.main()