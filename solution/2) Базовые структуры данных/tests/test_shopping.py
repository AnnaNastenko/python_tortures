#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import unittest

d = os.path.abspath(os.path.curdir)
sys.path.append(d)
from shopping import sweets


class TestShopping(unittest.TestCase):
    def setUp(self):
        self.id = {'карамель': [{'price': 41.99, 'shop': 'магнит'},
                                {'price': 45.99, 'shop': 'ашан'}],
                   'конфеты': [{'price': 30.99, 'shop': 'магнит'},
                               {'price': 32.99, 'shop': 'пятерочка'}],
                   'печенье': [{'price': 9.99, 'shop': 'пятерочка'},
                               {'price': 10.99, 'shop': 'ашан'}],
                   'пирожное': [{'price': 59.99, 'shop': 'пятерочка'},
                                {'price': 62.99, 'shop': 'магнит'}]}

        self.d = sweets

    def test_shop(self):
        self.assertDictEqual(self.id, self.d , msg="Сравнение словарей")


if __name__ == "__main__":
    unittest.main()
