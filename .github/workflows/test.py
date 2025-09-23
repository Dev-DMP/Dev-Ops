import unittest
import app  # importa o arquivo app.py

class TestApp(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(app.hello(), "Hello, DevOps!")

    def test_bye(self):
        self.assertEqual(app.bye(), "Goodbye, DevOps!")

    def test_hello_is_string(self):
        self.assertIsInstance(app.hello(), str)

    def test_bye_is_string(self):
        self.assertIsInstance(app.bye(), str)

    def test_hello_not_empty(self):
        self.assertNotEqual(app.hello(), "")

if __name__ == "__main__":
    unittest.main()
