#!/usr/bin/env python
#-*- coding: utf-8 -*-

import unittest
import os.path

from parser.xbrl import XBRL
# from nose.tools import *

class XbrlTestCase(unittest.TestCase):
    def testMultiplication(self):
        five = Xbrl(5)
        five.times(2)
        eq_(10, five.amount)

if __name__ == "__main__":
    unittest.main()
