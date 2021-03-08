#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import unittest

d = os.path.abspath(os.path.curdir)
sys.path.append(d)
from garden import garden_set, meadow_set, all_flowers, intersection, garden_diff, meadow_diff


class TestGarden(unittest.TestCase):
    def setUp(self):
        self.gs = garden_set
        self.ms = meadow_set
        self.af = all_flowers
        self.i = intersection
        self.gd = garden_diff
        self.md = meadow_diff

        self.igs = {'подсолнух', 'роза', 'ромашка', 'гладиолус', 'одуванчик'}
        self.ims = {'ромашка', 'мак', 'клевер', 'одуванчик'}
        self.iaf = {'клевер', 'подсолнух', 'роза', 'ромашка', 'гладиолус', 'мак', 'одуванчик'}
        self.ii = {'одуванчик', 'ромашка'}
        self.igd = {'гладиолус', 'роза', 'подсолнух'}
        self.imd = {'клевер', 'мак'}

    def test_garden_set(self):
        self.assertSetEqual(self.gs, self.igs, msg="Проверка множества <сад>")

    def test_meadow_set(self):
        self.assertSetEqual(self.ms, self.ims, msg="Проверка множества <луг>")

    def test_all_flowers(self):
        self.assertSetEqual(self.af, self.iaf, msg="Проверка общего множества")

    def test_intersection(self):
        self.assertSetEqual(self.i, self.ii, msg="Проверка пересечения")

    def test_diff_garden_meadow(self):
        self.assertSetEqual(self.gd, self.igd, msg="Растут в саду, но не растут на лугу")

    def test_diff_meadow_garden(self):
        self.assertSetEqual(self.md, self.imd, msg="Растут на лугу, но не растут в саду")


if __name__ == "__main__":
    unittest.main()