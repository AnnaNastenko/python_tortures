import os
import sys
import unittest

d = os.path.abspath(os.path.curdir)
sys.path.append(d)
import importlib
from operations import summ


class TestOperations(unittest.TestCase):
    def setUp(self):
        self.sa = summ

    def test_sum(self):
        self.assertEqual(self.sa, 25, msg="Результат для 1 2 3 4 5")


if __name__ == "__main__":
    unittest.main()
