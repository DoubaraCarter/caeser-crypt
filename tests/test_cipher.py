import unittest
from utils.cipher import caesar_cipher_encode, caesar_cipher_decode

class TestCaesarCipher(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(caesar_cipher_encode("ABC", 3), "DEF")
        self.assertEqual(caesar_cipher_encode("xyz", 3), "abc")
        self.assertEqual(caesar_cipher_encode("Hello, World!", 5), "Mjqqt, Btwqi!")

    def test_decode(self):
        self.assertEqual(caesar_cipher_decode("DEF", 3), "ABC")
        self.assertEqual(caesar_cipher_decode("abc", 3), "xyz")
        self.assertEqual(caesar_cipher_decode("Mjqqt, Btwqi!", 5), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
