import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)


class TestWithSetup(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3]

    def tearDown(self):
        self.data = None

    def test_lenght(self):
        self.assertEqual(len(self.data), 3)

    def test_max(self):
        self.assertEqual(max(self.data), 3)


if __name__ == "__main__":
    unittest.main()
