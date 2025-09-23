import unittest
from app import hello, bye

class TestApp(unittest.TestCase):

    def test_hello_returns_hello(self):
        self.assertEqual(hello(), "Hello, DevOps!")

    def test_bye_returns_goodbye(self):
        self.assertEqual(bye(), "Goodbye, DevOps!")

    def test_hello_not_empty(self):
        self.assertTrue(len(hello()) > 0)

    def test_bye_not_empty(self):
        self.assertTrue(len(bye()) > 0)

    def test_hello_type(self):
        self.assertIsInstance(hello(), str)

if __name__ == "__main__":
    unittest.main()
