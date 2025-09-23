# src/test.py
import unittest
from app import hello, bye

class TestApp(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello(), "Hello, DevOps!")

    def test_bye(self):
        self.assertEqual(bye(), "Goodbye, DevOps!")

    def test_hello_not_empty(self):
        self.assertNotEqual(hello(), "")

    def test_bye_not_empty(self):
        self.assertNotEqual(bye(), "")

    def test_hello_type(self):
        self.assertIsInstance(hello(), str)

if __name__ == "__main__":
    unittest.main()
