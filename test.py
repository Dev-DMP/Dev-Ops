import unittest
from app import hello, bye

class TestApp(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello(), "Hello, DevOps!")

    def test_bye(self):
        self.assertEqual(bye(), "Goodbye, DevOps!")

    def test_hello_type(self):
        self.assertIsInstance(hello(), str)

    def test_bye_type(self):
        self.assertIsInstance(bye(), str)

    def test_combined_length(self):
        combined = hello() + bye()
        self.assertTrue(len(combined) > 0)

if __name__ == "__main__":
    unittest.main()
