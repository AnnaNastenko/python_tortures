#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import unittest

d = os.path.abspath(os.path.curdir)
sys.path.append(d)
from store import tables_qty, tables_cost, sofas_qty, sofas_cost, chairs_qty, chairs_cost


class TestStore(unittest.TestCase):
    def setUp(self):
        # tables
        self.itq, self.itc = 54, 27860
        self.tq, self.tc = tables_qty, tables_cost
        # sofas
        self.isq, self.isc = 3, 3550
        self.sq, self.sc = sofas_qty, sofas_cost
        # chairs
        self.icq, self.icc = 105, 10311
        self.cq, self.cc = chairs_qty, chairs_cost

    def test_table(self):
        self.assertEqual(self.itq, self.tq, msg="Количество столов")
        self.assertEqual(self.itc, self.tc, msg="Стоимость столов")

    def test_sofa(self):
        self.assertEqual(self.isq, self.sq, msg="Количество диванов")
        self.assertEqual(self.isc, self.sc, msg="Стоимость диванов")

    def test_chair(self):
        self.assertEqual(self.icq, self.cq, msg="Количество стульев")
        self.assertEqual(self.icc, self.cc, msg="Стоимость стульев")


if __name__ == "__main__":
    unittest.main()