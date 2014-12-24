import unittest


def fun(x):
    return x + 1


def square(x):
    return x * x


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
    def testsquare(self):
        self.assertEqual(square(2), 4)

if __name__ == '__main__':
    unittest.main()


