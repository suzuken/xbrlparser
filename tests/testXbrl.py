#!/usr/bin/env python

from xbrl import *
from nose.tools import *

class TestXbrl():
    def testMultiplication(self):
        five = Xbrl(5)
        five.times(2)
        eq_(10, five.amount)

    def testParse():
        f = open('input/*')
        data = f.read()
        f.close()
        print type(data)
