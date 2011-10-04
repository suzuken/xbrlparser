#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Xbrl():
    def __init__(self, amount=0):
        self.amount = amount

    def times(self, multiplier):
        self.amount *= multiplier
