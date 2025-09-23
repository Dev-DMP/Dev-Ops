import unittest
from app import hello, bye, soma, subtrai, multiplica

class TestApp(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello(), "Hello, DevOps!")

    def test_bye(self):
        self.assertEqual(bye(), "Goodbye, DevOps!")

    def test_soma(self):
        self.assertEqual(soma(3, 2), 5)

    def test_subtrai(self):
        self.assertEqual(subtrai(10, 4), 6)

    def test_multiplica(self):
        self.assertEqual(multiplica(3, 5), 15)

if __name__ == "__main__":
    unittest.main()
