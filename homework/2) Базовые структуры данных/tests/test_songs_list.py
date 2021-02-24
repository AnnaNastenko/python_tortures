#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import unittest

d = os.path.abspath(os.path.curdir)
sys.path.append(d)
from songs_list import sum1, sum2


class TestSongs(unittest.TestCase):
    def setUp(self):
        self.s1 = sum1
        self.s2 = sum2

    def test_sum1(self):
        self.assertAlmostEqual(14.930000000000001, self.s1, msg="'Halo', 'Enjoy the Silence' и 'Clean'", places=1)

    def test_sum2(self):
        self.assertAlmostEqual(13.36, self.s2, msg="'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'", places=1)


if __name__ == "__main__":
    unittest.main()