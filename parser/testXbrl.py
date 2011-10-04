#!/usr/bin/env python
#-*- coding: utf-8 -*-

from xbrl import Xbrl
from nose.tools import *

class TestXbrl():
    def testMultiplication(self):
        five = Xbrl(5)
        five.times(2)
        eq_(10, five.amount)
