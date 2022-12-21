import unittest

from main import Application


class TestMain(unittest.TestCase):
    def test_application(self):
        Application()


if __name__ == '__main__':
    unittest.main()
