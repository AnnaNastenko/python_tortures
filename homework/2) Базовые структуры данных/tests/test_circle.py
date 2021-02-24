#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import unittest

d = os.path.abspath(os.path.curdir)
sys.path.append(d)
from circle import square, point_in, point2_in


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.sqr = square
        self.p_in = point_in
        self.p2_in = point2_in

    def test_circle_square(self):
        self.assertEqual(self.sqr, 5541.7693, msg="Площадь круга")

    def test_point_in(self):
        self.assertTrue(self.p_in, msg="Первая точка входит в состав круга?")

    def test_point2_in(self):
        self.assertFalse(self.p2_in, msg="Вторая точка входит в состав круга?")


if __name__ == "__main__":
    unittest.main()
