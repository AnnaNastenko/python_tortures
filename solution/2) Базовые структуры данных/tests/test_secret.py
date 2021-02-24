#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import unittest

d = os.path.abspath(os.path.curdir)
sys.path.append(d)
from secret import decode


class TestDecode(unittest.TestCase):
    def setUp(self):
        self.answer = 'в бане веник дороже денег'
        self.d = decode

    def test_decoding(self):
        self.assertEqual(self.d, self.answer, msg="Декодирование загадки")


if __name__ == "__main__":
    unittest.main()