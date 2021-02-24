#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import unittest

d = os.path.abspath(os.path.curdir)
sys.path.append(d)
from my_family import family_height, my_family_height


class TestFamily(unittest.TestCase):
    def setUp(self):
        self.fh = family_height

    def test_total_height(self):
        self.assertEqual(self.fh, sum(row[1] for row in my_family_height), msg="Проверка суммы роста семьи")


if __name__ == "__main__":
    unittest.main()