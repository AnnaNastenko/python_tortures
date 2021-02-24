#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import unittest

d = os.path.abspath(os.path.curdir)
sys.path.append(d)
from distance import moscow_london, moscow_paris, london_moscow, london_paris, paris_moscow, paris_london


class TestDistance(unittest.TestCase):
    def setUp(self):
        # M
        self.iml, self.imp = 145.60219778561037, 130.38404810405297
        # L
        self.ilp = 42.42640687119285
        # Internal
        self.ml = moscow_london
        self.lm = london_moscow

        self.mp = moscow_paris
        self.pm = paris_moscow

        self.lp = london_paris
        self.pl = paris_london

    def test_moscow(self):
        self.assertAlmostEqual(self.iml, self.ml, msg="Москва <-> Лондон", places=1)
        self.assertAlmostEqual(self.imp, self.mp, msg="Москва <-> Париж", places=1)

    def test_london(self):
        self.assertAlmostEqual(self.iml, self.lm, msg="Лондон <-> Москва", places=1)
        self.assertAlmostEqual(self.ilp, self.lp, msg="Лондон <-> Париж", places=1)

    def test_paris(self):
        self.assertAlmostEqual(self.imp, self.pm, msg="Париж <-> Москва", places=1)
        self.assertAlmostEqual(self.ilp, self.pl, msg="Париж <-> Лондон", places=1)


if __name__ == "__main__":
    unittest.main()




















class TestFavMovie(unittest.TestCase):
    def setUp(self):
        self.f = 145.60219778561037
        self.s = 145.6

    def test(self):
        self.assertAlmostEqual(self.f, self.s, places=1)


if __name__ == "__main__":
    unittest.main()