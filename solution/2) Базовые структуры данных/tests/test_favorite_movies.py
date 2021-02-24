#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import unittest

d = os.path.abspath(os.path.curdir)
sys.path.append(d)
from favorite_movies import first, second, penult, last


class TestFavMovie(unittest.TestCase):
    def setUp(self):
        self.fa = first
        self.sa = second
        self.pa = penult
        self.la = last

    def test_first_arg(self):
        self.assertEqual(self.fa, 'Терминатор', msg="Проверка первого фильма")

    def test_last_arg(self):
        self.assertEqual(self.la, 'Назад в будущее', msg="Проверка последнего фильма")

    def test_second_arg(self):
        self.assertEqual(self.sa, 'Пятый элемент', msg="Проверка второго фильма")

    def test_penult_arg(self):
        self.assertEqual(self.pa, 'Чужие', msg="Проверка предпоследнего фильма")


if __name__ == "__main__":
    unittest.main()