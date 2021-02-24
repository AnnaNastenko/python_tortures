#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import unittest

d = os.path.abspath(os.path.curdir)
sys.path.append(d)
from zoo import zoo, lion_cage, lark_cage


class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = zoo
        self.test_zoo = ['lion', 'bear', 'kangaroo', 'monkey', 'rooster', 'ostrich', 'lark']
        self.lc = lion_cage
        self.lr_c = lark_cage

    def test_zoo(self):
        self.assertListEqual(self.zoo, self.test_zoo, msg="Итоговый зоопарк")

    def test_lion(self):
        self.assertEqual(self.lc, 1, msg="Клетка льва")

    def test_lark(self):
        self.assertEqual(self.lr_c, 7, msg="Клетка жаворонка")


if __name__ == "__main__":
    unittest.main()